# Use a slim Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies (Chrome + drivers)
RUN apt-get update && \
    apt-get install -y wget curl gnupg unzip && \
    curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    
# Copy the entire project folder into /app
COPY . .

# Go into the folder where app.py exists
WORKDIR /app/merged

# Expose the port Flask uses
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
