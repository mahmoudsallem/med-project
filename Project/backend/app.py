from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import redis
import os
import json

# Flask backend application
app = Flask(__name__)

# CORS Configuration - Only allow requests from your frontend
# In production, replace '*' with your actual frontend domain
CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv("ALLOWED_ORIGINS", "*").split(","),
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": False
    }
})

# Security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

pg_conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)

cur = pg_conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT,
  job TEXT,
  email TEXT
)
""")
pg_conn.commit()

@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.json
    
    # Input validation
    if not data or not all(k in data for k in ["name", "job", "email"]):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Basic email validation
    if "@" not in data["email"]:
        return jsonify({"error": "Invalid email format"}), 400
    
    try:
        cur.execute(
            "INSERT INTO users (name, job, email) VALUES (%s,%s,%s)",
            (data["name"], data["job"], data["email"])
        )
        pg_conn.commit()
        redis_client.delete("users")
        return jsonify({"status": "ok"})
    except Exception as e:
        pg_conn.rollback()
        return jsonify({"error": "Database error"}), 500



@app.route("/api/users", methods=["GET"])
def get_users():
    cached = redis_client.get("users")
    if cached:
        try:
            return jsonify(json.loads(cached))
        except json.JSONDecodeError:
            redis_client.delete("users") # Clear bad cache

    cur.execute("SELECT name, job, email FROM users")
    rows = cur.fetchall()
    users = [{"name": r[0], "job": r[1], "email": r[2]} for r in rows]
    
    # Use standard JSON serialization
    redis_client.set("users", json.dumps(users))
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
