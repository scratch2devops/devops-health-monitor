from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/")
def health():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    return f"""
    <h1>DevOps Health Monitor</h1>
    <p>CPU Usage: {cpu}%</p>
    <p>Memory Usage: {memory}%</p>
    """

app.run(host="0.0.0.0", port=8000)