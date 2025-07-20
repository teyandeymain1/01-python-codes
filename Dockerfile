# -------------------------------下記はPythonのバージョンが変わるごとに変更して-------------------------------
FROM python:3.13-slim-bookworm
# -------------------------------上記はPythonのバージョンが変わるごとに変更して-------------------------------


# -------------------------------下記は変更禁止-------------------------------
# set language environment
ENV LANG=C.UTF-8
# set non-root user
ARG USERNAME=python_with_docker

    # install git and create user and group
RUN apt-get update &&\
    apt-get install -y git &&\
    groupadd -r $USERNAME &&\
    useradd -r -m -g $USERNAME $USERNAME &&\  
    rm -rf /var/lib/apt/lists/*

# set user
USER $USERNAME

WORKDIR /home/$USERNAME