FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the source code
COPY . .

# Run Django migrations
RUN cd ./core && python manage.py makemigrations && python manage.py migrate

# Expose the application's port
EXPOSE 8000

# Run the application
CMD ["python", "./core/manage.py", "runserver", "0.0.0.0:8000"]
