# Dockerfile

# Use the official Python base image
FROM python:3.8

# Set the working directory in the Docker image
WORKDIR /app

# Copy your Python file and other necessary files to the Docker image
COPY app.py ./

# Install psycopg library
RUN apt-get update && apt-get install -y net-tools && apt-get install -y iputils-ping
RUN pip install psycopg2
RUN pip install flask

EXPOSE 8081

# Define the command to run your Python file
CMD ["python", "app.py"]
#CMD ["flask", "run", "--host=0.0.0.0", "--port=8081"]
