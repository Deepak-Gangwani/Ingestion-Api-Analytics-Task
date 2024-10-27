from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory storage for machine data and status
processed_data = []
machine_status = "IDLE"
allowed_statuses = {"STARTED", "RUNNING", "COMPLETED", "IDLE"}

# Serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')  # This will look for index.html in a "templates" folder

# Endpoint to get all processed data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(processed_data), 200

# Endpoint to add new data
@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.json
    processed_data.append(new_data)
    return jsonify({"message": "Data added successfully"}), 200

# Endpoint to get or update the machine status
@app.route('/status', methods=['GET', 'POST'])
def update_status():
    global machine_status
    if request.method == 'POST':
        new_status = request.json.get("status")
        if new_status not in allowed_statuses:
            return jsonify({"error": "Invalid status"}), 400
        machine_status = new_status
        return jsonify({"status": machine_status}), 200
    else:
        return jsonify({"status": machine_status}), 200

# Custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page Not Found"}), 404  # You can also render a custom HTML template here

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
