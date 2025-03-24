# Pull official base image
FROM python:3.12.9-alpine

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Copy project
COPY . /usr/src/app/

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]