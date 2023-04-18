FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# ENV POSTGRES_HOST=<your-postgres-container-name>
# ENV POSTGRES_PORT=<your-postgres-port>
# ENV POSTGRES_DB=<your-postgres-db-name>
# ENV POSTGRES_USER=<your-postgres-username>
# ENV POSTGRES_PASSWORD=<your-postgres-password>

EXPOSE 5433 
#COPY extract.py .

#CMD ["python", "createTables.py"]