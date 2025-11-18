import docker
# We need Response and stream_with_context for real-time streaming
from flask import Flask, jsonify, send_file, request, Response, stream_with_context
from flask_cors import CORS

# --- Setup ---
app = Flask(__name__)
CORS(app)

try:
    client = docker.from_env()
    client.ping()
    print("✅ Successfully connected to Docker daemon.")
except Exception as e:
    print(f"❌ Failed to connect to Docker daemon. Is it running?")
    print(f"Error: {e}")
    client = None

# --- API Endpoints ---

@app.route('/api/containers')
def get_containers():
    if not client:
        return jsonify({"error": "Docker daemon not available"}), 503
    try:
        containers = client.containers.list(all=True)
        container_list = []
        for container in containers:
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

@app.route('/api/containers/<container_id>/<action>', methods=['POST'])
def container_action(container_id, action):
    if not client:
        return jsonify({"error": "Docker daemon not available"}), 503
    try:
        container = client.containers.get(container_id)
        if action == 'start':
            container.start()
            message = f"Container {container.name} started successfully."
        elif action == 'stop':
            container.stop()
            message = f"Container {container.name} stopped successfully."
        elif action == 'remove':
            container.remove()
            message = f"Container {container.name} removed successfully."
        else:
            return jsonify({"error": "Invalid action"}), 400
        return jsonify({"message": message})
    except docker.errors.NotFound:
        return jsonify({"error": "Container not found"}), 404
    except docker.errors.APIError as e:
        return jsonify({"error": str(e)}), 409 
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- UPDATED: Real-Time Log Streaming Endpoint ---
@app.route('/api/containers/<container_id>/logs_stream')
def stream_container_logs(container_id):
    """
    Streams logs in real-time using Server-Sent Events (SSE).
    """
    def generate():
        try:
            container = client.containers.get(container_id)
            # stream=True: keeps connection open
            # follow=True: waits for new logs
            # tail=100: Start with the last 100 lines so the window isn't empty
            for line in container.logs(stream=True, follow=True, tail=100):
                # SSE format requires "data: <content>\n\n"
                yield f"data: {line.decode('utf-8')}\n\n"
        except Exception as e:
            yield f"data: Error streaming logs: {str(e)}\n\n"

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

# --- Frontend Route ---

@app.route('/')
def serve_frontend():
    return send_file('index.html')

if __name__ == '__main__':
    print("🚀 Starting Flask server... Open http://127.0.0.1:5000 in your browser.")
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)