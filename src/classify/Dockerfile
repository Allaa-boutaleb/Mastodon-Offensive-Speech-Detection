# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app/classify

# Copy the current directory contents into the container at /app/classify
COPY classify/ .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Run main.py when the container launches
CMD ["python", "main.py"]
