# Base Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy backend code to container
COPY . .

# Install required system packages: C/C++ compilers, Java, and necessary tools
RUN apt-get update && apt-get install -y \
    build-essential \
    default-jdk \
    nodejs \
    npm \
    gcc \
    g++ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir flask flask-cors

# Expose backend port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
