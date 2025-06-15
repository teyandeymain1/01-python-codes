# -------------------------------下記はPythonのバージョンが変わるごとに変更して-------------------------------


FROM python:3.13-slim-buster

# -------------------------------下記は変更禁止-------------------------------

ENV LANG=C.UTF-8

# set non-root user
ARG USERNAME=Python_Docker
# set local directory
ARG LOCAL_DIR=/Users/teyan/Desktop/Programming/Codes/6_C_Codes

    # create user and group
RUN groupadd -r $USERNAME &&\
    useradd -r -g $USERNAME $USERNAME &&\  
    rm -rf /var/lib/apt/lists/*

# set user
USER $USERNAME

WORKDIR $LOCAL_DIR