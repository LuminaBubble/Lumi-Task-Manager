from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/schedule', methods=['POST'])
def schedule():
    data = request.json
    return jsonify({
        "status": "success",
        "message": "Schedule optimized",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)
