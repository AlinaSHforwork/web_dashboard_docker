import docker
from flask import Flask, jsonify, send_file
from flask_cors import CORS

# --- Setup ---
app = Flask(__name__)
# Enable CORS (Cross-Origin Resource Sharing)
# This lets our index.html talk to our app.py on the same machine
CORS(app)

try:
    # Connect to the Docker daemon
    client = docker.from_env()
    client.ping()
    print("✅ Successfully connected to Docker daemon.")
except Exception as e:
    print(f"❌ Failed to connect to Docker daemon. Is it running?")
    print(f"Error: {e}")
    # In a real app, you'd handle this more gracefully
    client = None

# --- API Endpoints ---

@app.route('/api/containers')
def get_containers():
    """
    API endpoint to get a list of all containers (running and stopped).
    """
    if not client:
        return jsonify({"error": "Docker daemon not available"}), 503

    try:
        # Get all containers (all=True includes stopped ones)
        containers = client.containers.list(all=True)
        
        # Format the data into a simple list of dictionaries for our frontend
        container_list = []
        for container in containers:
            # Get the first image tag, if it exists
            image_tag = container.image.tags[0] if container.image.tags else 'N/A'
            
            container_list.append({
                "id": container.short_id,
                "name": container.name,
                "image": image_tag,
                "status": container.status
            })
            
        return jsonify(container_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Frontend Route ---

@app.route('/')
def serve_frontend():
    """
    Serves the main index.html file.
    """
    return send_file('index.html')

# --- Run the App ---

if __name__ == '__main__':
    print("🚀 Starting Flask server... Open http://127.0.0.1:5000 in your browser.")
    # host='0.0.0.0' makes it accessible on your local network
    app.run(host='0.0.0.0', port=5000, debug=True)