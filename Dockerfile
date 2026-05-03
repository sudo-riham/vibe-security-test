# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Create a non-root user and switch to it
# This prevents attackers from gaining root access
# if they ever break into the container
RUN useradd --create-home --shell /bin/bash appuser
USER appuser

# Tell the container what port to listen on
EXPOSE 8080

# Default command
CMD ["python", "-m", "http.server", "8080"]
