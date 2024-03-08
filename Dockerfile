# Use Python base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY script.py /app/script.py
RUN mkdir -p text_files

COPY text_files/file1.txt text_files/file1.txt
COPY text_files/file2.txt text_files/file2.txt
COPY text_files/file3.txt text_files/file3.txt
COPY text_files/file4.txt text_files/file4.txt

# Install dependencies
RUN pip install --no-cache-dir numpy flask

#Set environments for docker container (default word count = 4)
ENV FILE_PATHS " "
ENV NUMOFWORDS 4 
# Expose port 8080
EXPOSE 8080

# Command to run the Flask web server
CMD ["python", "script.py"]
