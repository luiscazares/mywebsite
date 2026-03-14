🌐 Minimalist Cyber-Portfolio

A high-performance, containerized personal portfolio built with Django, featuring real-time system telemetry and a cloud-exposed local tunnel.

🚀 The Stack

    Backend: Django 5.x (Python)

    Frontend: Bootstrap 5 (Custom "Cyber-Minimalist" CSS)

    Monitoring: psutil (System Sentinel)

    Infrastructure: Docker & Docker Compose

    Environment: WSL2 (Windows Subsystem for Linux)

    Networking: Cloudflare Tunnel (Zero Trust)

🛠 Project Apps

📡 System Sentinel
A real-time telemetry dashboard.

    Interfaces directly with the host kernel via psutil.

    Monitors CPU load, RAM usage, Network I/O, and System Uptime.

    Displays visitor metadata (IP and User-Agent) for connection debugging.

🖼 Gallery
A dynamic project showcase.

    Database-driven project management via Django Admin.

    Supports image uploads (Pillow) and project categorization.

    Clean, responsive grid layout with Glassmorphism hover effects.

✍️ Blog (WIP)

    Markdown-supported technical writing platform.

    Category tagging and chronological archival.

🏗 Infrastructure & Deployment
This project is hosted on a Home Lab setup rather than a traditional VPS.

1. The Containerized Environment
The application is fully containerized using Docker. This ensures that the Python environment, database, and static file handlers (WhiteNoise) remain consistent regardless of the host machine.

2. WSL2 Bridge
The project runs inside a WSL2 (Ubuntu) instance on a physical Windows machine. This allows for native Linux performance and Docker integration while utilizing local hardware for the "Sentinel" metrics.

3. Cloudflare Tunnel (The "Zero Trust" Pipe)
Instead of opening insecure ports on a home router, this site uses a cloudflared tunnel.

    Security: No inbound ports are open (No port forwarding).

    Privacy: The home IP address remains hidden behind Cloudflare’s edge nodes.

    SSL: End-to-end encryption is handled automatically by the tunnel.
   

🔧 Local Development Setup

  1. Clone the Repo:

    git clone https://github.com/yourusername/portfolio-project.git

  2. Environment Variables: Create a .env file in the root:

    DEBUG=True
    SECRET_KEY=your_secret_key
    OPENWEATHER_API_KEY=your_key

  3. Run with Docker:

    docker compose up --build

📈 Future Roadmap

    [ ] Integrate Chart.js for historical CPU data in Sentinel.

    [ ] Add Dark/Light mode toggle based on CSS variables.

    [ ] Implement automated PostgreSQL backups to S3.
