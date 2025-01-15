from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/task', methods=['POST'])
def prioritize_task():
    data = request.json
    return jsonify({"message": "Task prioritized", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
