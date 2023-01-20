FROM  mcr.microsoft.com/playwright:v1.27.0-focal

RUN apt update
RUN apt install -y sudo make apt-utils python3 python3-venv python3-pip
RUN echo 'ALL ALL=NOPASSWD:ALL' >> /etc/sudoers
