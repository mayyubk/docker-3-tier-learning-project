# 3-Tier Web Application with Docker Compose

This is a complete 3-tier web application built to practice and demonstrate core DevOps and containerization concepts. The entire application stack (Frontend, Backend, Database) is fully containerized using Docker and orchestrated with a single Docker Compose file.

## 📜 Description

The application consists of three independent services:

1.  **Frontend (Tier 1):** A static `index.html` page served by an **Nginx** container. This container also acts as a reverse proxy, forwarding all API requests to the backend service.
2.  **Backend (Tier 2):** A **Python Flask** API that serves as the "brain" of the application. It receives requests from the frontend and communicates with the database to fetch or store data.
3.  **Database (Tier 3):** A **PostgreSQL** database container that persistently stores all application data using a named Docker volume.

## ✨ Features

* **Fully Containerized:** Each service runs in its own isolated Docker container.
* **Service Orchestration:** A single `docker-compose.yml` file manages the build, networking, and lifecycle of all three services.
* **Reverse Proxy:** Nginx is configured to serve the frontend *and* route `/api/` requests to the backend, all from a single entry point (`localhost:3000`).
* **Service Discovery:** The frontend and backend services communicate with each other using their Docker service names (e.g., `backend`, `database`).
* **Persistent Data:** A Docker **volume** is used for the PostgreSQL database to ensure that data persists even if the container is stopped or removed.

## 📂 Project Structure

```bash
/
├── .gitignore             # Tells Git which files to ignore
├── docker-compose.yml     # The master file for all services
├── README.md              # This project description file
│
├── backend-api/           # The Python backend service
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
│
└── frontend-app/          # The Nginx frontend service
    ├── Dockerfile
    ├── index.html
    └── nginx.conf




## 🚀 How to Run

Before you begin, ensure you have **Docker** and **Docker Compose** installed on your system.

1. Clone the Repository
```bash
git clone [https://github.com/mayyubk/docker-3-tier-learning-project.git](https://github.com/mayyubk/docker-3-tier-learning-project.git)
cd docker-3-tier-learning-project

2. Build and Run the Application From the root directory (where docker-compose.yml is located), run:
docker compose up --build

3. Access the Application Once all containers are running, open your web browser and navigate to:
 http://localhost:3000
You can test the full stack by clicking the "Test Database Connection" button, which demonstrates the full Frontend -> Backend -> Database communication flow.

4. Stop the Application To stop and remove all containers, networks, and volumes, press Ctrl+C in the terminal and then run
docker compose down

## 🧠 Key Learning Outcomes
This project is a practical exercise in understanding the following concepts:

 **Dockerfile Creation:** Writing separate, optimized Dockerfiles for a frontend (Nginx) and backend (Python) application.
 **Docker Compose:** Defining and linking multiple services, managing environment variables, and orchestrating a complete stack.
 **Nginx Configuration:** Writing a custom `nginx.conf` to serve static files and act as a reverse proxy.
 **Container Networking:** Understanding how containers on the same Docker network can resolve each other by name.
 **Data Persistence:** Using Docker volumes to manage the state and data of a stateful service like a database.
 **Troubleshooting:** Using `docker compose logs` to debug issues across multiple services (e.g., Nginx 502 errors, Python connection failures).

