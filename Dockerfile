# Use an official Python runtime as the base image
FROM python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . /app/


RUN apt-get update \
    && apt-get upgrade -y 
    

RUN pip3 install --no-cache-dir -r /app/requirements.txt
# Command to run the FastAPI application using Uvicorn server
CMD ["python", "app.py"]