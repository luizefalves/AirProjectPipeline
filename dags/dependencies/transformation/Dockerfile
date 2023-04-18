# Use the official Python base image
FROM python:3.8

# Set the working directory in the Docker image
WORKDIR /app

# Copy your Python file and other necessary files to the Docker image
COPY your_python_file.py .

# Install psycopg library
RUN pip install psycopg2

# Define the command to run your Python file
CMD ["python", "your_python_file.py"]