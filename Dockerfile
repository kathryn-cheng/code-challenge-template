FROM continuumio/miniconda3:latest

# install conda to aid in installation of binary dependencies.
RUN conda install -y 'python>=3.11,<3.12' psycopg2 pandas

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

EXPOSE 8000

# Specify the command to run on container start
CMD ["python", "-m", "uvicorn", "--host", "0.0.0.0", "weather_monitor.main:app"]

