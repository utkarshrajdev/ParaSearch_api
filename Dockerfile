# Use the official Python image as a base
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /word_api

# Install dependencies
COPY requirements.txt /word_api/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /word_api/
