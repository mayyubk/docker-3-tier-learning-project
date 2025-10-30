# Base image 
FROM python:3.9-slim

# Set Working Diractory inside the container
WORKDIR app

# Copy dependencies 
COPY requirements.txt .

# Install  dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application's code 
COPY . .

# Expose the port application run on 
EXPOSE 5000

#The command to run the aplication
CMD ["python", "app.py"]









