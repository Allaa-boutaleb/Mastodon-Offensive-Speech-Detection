# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app/

# Install any needed packages specified in requirements.txt
# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the current directory contents into the container at /app/classify
COPY . .

# Run main.py when the container launches
CMD ["python", "main.py"]
