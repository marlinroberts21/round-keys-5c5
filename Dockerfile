FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip

RUN apt install -y git

RUN git clone https://github.com/marlinroberts21/round-keys-5c5.git

WORKDIR /round-keys-5c5

RUN /bin/bash

