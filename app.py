from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import os

# Flask ko batana ki hamari HTML aur CSS isi folder mein hain
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    # Aapki HTML file ka naam yahan load hoga
    return render_template('login page01.html')

# Aapki CSS file (style001.css) ko link karne ke liye route
@app.route('/style001.css')
def css():
    return send_from_directory('.', 'style001.css')

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Yahan Python validation (Double check)
        # Note: JavaScript se signal aate hi ye function game start karega
        if username and password:
            # Aapki game file (mysnake.py) ko naye window mein kholna
            # 'python' command tabhi kaam karegi jab aapka python path set ho
            subprocess.Popen(['python', 'mysnake.py']) 
            
            return jsonify({
                "status": "success", 
                "message": f"Login Successful! Opening Snake World for {username}..."
            })
        else:
            return jsonify({"status": "error", "message": "Invalid Data Received!"})
            
    except Exception as e:
        return jsonify({"status": "error", "message": f"Server Error: {str(e)}"})

if __name__ == '__main__':
    print("--- Flask Server Starting ---")
    print("Open Chrome and go to: http://127.0.0.1:5000")
    app.run(debug=True)
