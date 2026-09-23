from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/health")
def health():
    health = {
        "status": "healthy",
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent
    }
    return health
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)