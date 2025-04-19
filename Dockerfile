# Use a slim Python image
FROM python:3.10-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:99

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements first (for caching)
COPY requirements.txt .

# Install Python and system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    wget \
    unzip \
    xvfb \
    x11-utils \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    fonts-liberation \
    && pip install --no-cache-dir -r requirements.txt

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Copy the entire project folder into /app
COPY . .

# Go into the folder where app.py exists
WORKDIR /app/merged

# Expose the port Flask uses
EXPOSE 5000

# Start Xvfb and then run the app
CMD xvfb-run --server-args="-screen 0 1920x1080x24" python app.py
