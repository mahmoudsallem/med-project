from flask import Flask, request, jsonify
import psycopg2
import redis
import os
import json

# Flask backend application
app = Flask(__name__)

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
    cur.execute(
        "INSERT INTO users (name, job, email) VALUES (%s,%s,%s)",
        (data["name"], data["job"], data["email"])
    )
    pg_conn.commit()
    redis_client.delete("users")
    return jsonify({"status": "ok"})

import json

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
