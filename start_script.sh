#!/bin/bash

# Find the database IP adress from image name
read -p "Enter the name of the database image (default: postgres:13-alpine): " image_name
image_name=${image_name:-"postgres:13-alpine"}

# Read boolean input to decide whether to run 'docker-compose up'
read -p "Do you want to run 'docker-compose up' ? (True/False): " runit

# Check if runit input is valid 
if [[ "$runit" != "True" && "$runit" != "False" ]]; then
  echo "Invalid input! Please enter either 'True' or 'False'."
  exit 1
fi

# Run 'docker-compose up' or not based on input
if [ "$runit" == "True" ]; then
  docker-compose up -d "$image_name" 
else
  echo "Ok!"
fi

# Find the container ID associated with the image name
container_id=$(docker ps -a | grep "$image_name" | awk '{ print $1 }')

# Check if container ID is empty
if [ -z "$container_id" ]; then
  echo "No container found for image: $image_name"
  exit 1
fi

# Run docker inspect with container ID and use jq to extract IP address
ip_address=$(docker inspect "$container_id" | jq -r '.[0].NetworkSettings.Networks | .[].IPAddress')

# Check if IP address is empty
if [ -z "$ip_address" ]; then
  echo "Failed to extract IP address for container: $container_id"
  exit 1
fi


# Find the container name containing the string "scheduler"
scheduler_container_name=$(docker ps -a --format "{{.Names}}" | grep "scheduler" 2> /dev/null)

# Check if scheduler container name is empty
if [ -z "$scheduler_container_name" ]; then
  echo "No container found with the name containing 'scheduler'"
  exit 1
fi

# Trigger the DAG in the scheduler container
docker exec -it "$scheduler_container_name" airflow dags trigger first_sample_dag 

# Display the IP address as the database's IP address
echo "This is the IP address of your database: $ip_address"
