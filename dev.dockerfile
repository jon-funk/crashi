FROM python:3.9.1 as runtime
RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Setup user to represent developer permissions in container
ARG USERNAME=python
ARG USER_UID=1000
ARG USER_GID=1000
RUN useradd -rm -d /home/$USERNAME -s /bin/bash -g root -G sudo -u $USER_UID $USERNAME
USER $USERNAME

EXPOSE 5005