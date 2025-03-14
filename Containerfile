FROM registry.redhat.io/ubi9/python-39

# Set the working directory.
WORKDIR /app

# Copy the dependency file and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Expose the port the app runs on.
EXPOSE 8080

# Set the environment variable for Flask to run on port 8080.
ENV FLASK_RUN_PORT=8080
ENV FLASK_APP=ask-llm.py

# Run the application.
CMD ["flask", "run", "--host=0.0.0.0"]