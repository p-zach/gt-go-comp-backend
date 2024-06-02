from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/get_response/<pos>')
def get_response(pos: str):
        x, y = pos.split('_')
        x = int(x)
        y = int(y)
        x += 1
        y += 1
        response = {'x': x, 'y': y}
        return json.dumps(response)

if __name__ == "__main__":
    app.run()