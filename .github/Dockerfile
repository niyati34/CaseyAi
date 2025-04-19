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

# Move into the folder that contains app.py
WORKDIR /app/merged

# Expose the port Flask or your app uses
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
