# Use a slim Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies (Chrome + drivers)
RUN apt-get update && apt-get install -y wget unzip && \
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &
apt install -y/google-chrome-stable_current_amd64.deb && \
rm google-chrome-stable_current_amd64.deb && \
apt-get clean

    
# Copy the entire project folder into /app
COPY . .

# Go into the folder where app.py exists
WORKDIR /app/merged

# Expose the port Flask uses
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
