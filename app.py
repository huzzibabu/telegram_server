from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Get raw data from the request
        raw_data = request.get_data(as_text=True)
        print(f'Raw data received: {raw_data}')
        
        # Parse JSON data
        json_data = request.get_json(force=True)
        print(f'JSON data: {json_data}')
        
        # Extract the message from the JSON data
        message = json_data.get('message')
        print(f'Received message: {message}')
        
        if message:
            # Run a subprocess with the received message
            result = subprocess.run(['python', 'send_message.py', message], capture_output=True, text=True)
            print(f'Result: {result.stdout}, Error: {result.stderr}')
            return jsonify({"status": "success", "message": result.stdout}), 200
        else:
            return jsonify({"status": "error", "message": "No message"}), 400
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
