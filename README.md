<h1>🐳 Simple Docker Dashboard</h1>

<p>A lightweight, real-time web dashboard for managing Docker containers.</p>

<p>This project demonstrates how to interact programmatically with the Docker Engine API using Python. It provides a clean web interface to view running containers, control their state (start/stop/remove), and stream logs in real-time.</p>

<h2>✨ Features</h2>
    <ul>
        <li><strong>Live Container List:</strong> View all running and stopped containers with their status and image names.</li>
        <li><strong>Container Management:</strong>
            <ul>
                <li>▶️ <strong>Start</strong> stopped containers.</li>
                <li>⏹️ <strong>Stop</strong> running containers.</li>
                <li>🗑️ <strong>Remove</strong> containers (with confirmation).</li>
            </ul>
        </li>
        <li><strong>📡 Real-Time Log Streaming:</strong> View live logs from any container using Server-Sent Events (SSE), just like <code>docker logs -f</code>.</li>
        <li><strong>Modern UI:</strong> Built with Tailwind CSS for a responsive, dark-mode interface.</li>
    </ul>

<h2>🛠️ Technologies Used</h2>
    <ul>
        <li><strong>Backend:</strong> Python, Flask</li>
        <li><strong>Docker Integration:</strong> Docker SDK for Python (<code>docker</code>)</li>
        <li><strong>Frontend:</strong> HTML5, JavaScript (Vanilla), Tailwind CSS (CDN)</li>
        <li><strong>Communication:</strong> REST API, Server-Sent Events (SSE)</li>
    </ul>

<h2>⚙️ Prerequisites</h2>
    <ul>
        <li><strong>Docker:</strong> Ensure Docker Desktop (Mac/Windows) or Docker Engine (Linux) is installed and running.</li>
        <li><strong>Python 3.x</strong></li>
    </ul>

<h2>🚀 Installation & Setup</h2>
    <ol>
        <li>
            <strong>Clone the repository</strong> (or download the files):
            <pre><code>git clone &lt;https://github.com/AlinaSHforwork/web_dashboard_docker&gt;
cd docker-dashboard</code></pre>
        </li>

<li>
            <strong>Create a Virtual Environment:</strong>
            <p>It is recommended to use a virtual environment to keep dependencies clean.</p>
            <pre><code># Create the venv
python3 -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate</code></pre>
        </li>

<li>
            <strong>Install Dependencies:</strong>
            <pre><code>pip install docker flask flask-cors</code></pre>
        </li>
    </ol>

<h2>🏃‍♂️ How to Run</h2>
    <ol>
        <li>
            <strong>Ensure Docker is running.</strong>
            <p><em>Linux users:</em> You may need to add your user to the docker group or run with access to the Docker socket.</p>
        </li>

 <li>
            <strong>Start the Flask Server:</strong>
            <pre><code>python3 app.py</code></pre>
            <p>You should see output indicating the server has started:</p>
            <blockquote>🚀 Starting Flask server... Open http://127.0.0.1:5000 in your browser.</blockquote>
        </li>

  <li>
            <strong>Open the Dashboard:</strong>
            <p>Open your web browser and navigate to: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a></p>
        </li>
    </ol>

 <h2>🧪 Testing</h2>
    <p>To see the dashboard in action, you can spin up a test container in a separate terminal:</p>
    <pre><code># Run a simple Nginx web server
docker run -d --name test-nginx -p 8080:80 nginx</code></pre>
    <p>Refresh your dashboard, and you will see <code>test-nginx</code> appear in the list!</p>

 <h2>🛡️ Troubleshooting</h2>
    <ul>
        <li><strong>"Failed to connect to Docker daemon":</strong> Make sure Docker Desktop is open and running. On Linux, check permissions for <code>/var/run/docker.sock</code>.</li>
        <li><strong>Circular Import Error:</strong> Ensure you import <code>Flask</code> from <code>flask</code> and not from your own file name.</li>
    </ul>
