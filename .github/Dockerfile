# Use a slim Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project folder into /app
COPY . .

# Go into the folder where app.py exists
WORKDIR /app/merged

# Expose the port Flask uses
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
