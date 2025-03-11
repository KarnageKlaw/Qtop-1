from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Fetch system username
    username = os.getenv('USER') or os.getenv('USERNAME') or 'Unknown'

    # Fetch full name (Replace with your actual name)
    full_name = "Your Full Name"

    # Get system time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Run top command and capture output
    top_output = subprocess.getoutput("top -b -n 1")

    # Generate HTML output
    return f"""
    <html>
    <body>
        <h2>Name: {full_name}</h2>
        <h3>Username: {username}</h3>
        <h3>Server Time (IST): {server_time}</h3>
        <h3>TOP output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
