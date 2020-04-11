FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Copy requirements
COPY requirements.txt /

# Copy entrypoint script and set execution permission
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Install dependencies.
RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code

# Copy project code.
COPY . /code/

EXPOSE 80