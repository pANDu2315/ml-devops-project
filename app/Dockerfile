# Use the official lightweight Python 3.10 image as the base image
# "slim" reduces image size by excluding unnecessary packages
FROM python:3.10-slim

# Set the working directory inside the container to /app
# All subsequent commands will be executed from this directory
WORKDIR /app

# Copy the requirements file from the host machine to the container
# This file contains all Python dependencies for the application
COPY requirements.txt .

# Install the Python dependencies listed in requirements.txt
# --no-cache-dir prevents pip from storing cache files, reducing image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code (app.py) from the host to the container
COPY app.py .

# Expose port 5000 to allow external access to the application
# This is typically used for Flask or similar web frameworks
EXPOSE 5000

# Define the default command to run when the container starts
# This runs the Python application
CMD ["python", "app.py"]
