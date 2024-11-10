# Use a Python image
FROM python:3.12.7-bullseye

# Set the working directory
WORKDIR /usr/src/djangobnb_backend

# Install system dependencies
# RUN apt-get update && apt-get install -y libpq-dev


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY ./entrypoint.sh .
COPY ./entrypoint.sh /usr/src/djangobnb_backend/entrypoint.sh

RUN sed -i 's/\r$//g' /usr/src/djangobnb_backend/entrypoint.sh
# RUN chmod +x /usr/src/djangobnb_backend/entrypoint.sh
RUN chmod +x /usr/src/djangobnb_backend/entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/src/djangobnb_backend/entrypoint.sh" ]