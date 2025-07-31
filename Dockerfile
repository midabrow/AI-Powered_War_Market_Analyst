# Set the python version as a build-time argument
# with Python 3.11 as the default
ARG PYTHON_VERSION=3.11-slim
FROM python:${PYTHON_VERSION}

# Upgrade pip
RUN pip install --upgrade pip

# Install Git and build tools, then clean up to reduce image size
RUN apt-get update && apt-get install -y \
    git build-essential && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container to /app
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the entire project code into the container's working directory
COPY . /app

# COPY data/faiss_store.pkl /app/data/faiss_store.pkl

# Clean up apt cache to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
