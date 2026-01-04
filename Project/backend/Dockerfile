FROM python:3.13-slim
WORKDIR /app
# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --group appuser

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Switch to non-root user
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
