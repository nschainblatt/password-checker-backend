from flask import Flask, request
from flask_cors import CORS
import checker

app = Flask(__name__)
CORS(app)

@app.route("/checkpassword", methods = ['POST', 'GET'])
def get_password():
    if request.method == 'POST':
        password = request.get_json()['password']
        status, data = checker.main(password)
        if status:
            return {"status": True, "count": data}
        else:
            return {"status": False, "password": data}
    else:
        return {"status": "failed"}
    

if __name__ == "__main__":
	app.run(host='0.0.0.0')
