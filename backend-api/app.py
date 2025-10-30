import os
import time
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    # These environment variables come from docker-compose.yml
    host = os.environ.get('DB_HOST')
    dbname = os.environ.get('POSTGRES_DB')
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    
    # Retry connecting to the database
    # This gives the DB container time to start up
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=host,
                dbname=dbname,
                user=user,
                password=password
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            print(f"Database not ready, retrying... ({retries} attempts left)")
            time.sleep(5)
    
    raise Exception("Could not connect to database.")

@app.route('/')
def hello():
    return "Hello from the Backend API!"

@app.route('/db_status')
def db_status():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify(message="Database connection successful!"), 200
    except Exception as e:
        return jsonify(message=f"Database connection failed: {e}"), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
