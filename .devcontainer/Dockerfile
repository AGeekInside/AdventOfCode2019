#ARG PYTHON_VERSION=3.7.4-buster
ARG DEBIAN_VERSION=buster
FROM debian:${DEBIAN_VERSION}
ARG MAINTAINER="AGeekInside <marcwbrooks@gmail.com>"
LABEL MAINTAINER $(MAINTAINER)

ENV DEBIAN_FRONTEND noninteractive

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && apt-get install -y \
  apt-utils \
  build-essential \
  curl \
  git \
  wget \
  && rm -rf /var/lib/apt/lists/*

# Install bat
RUN wget --no-check-certificate https://github.com/sharkdp/bat/releases/download/v0.11.0/bat_0.11.0_amd64.deb \
  && wget --no-check-certificate https://github.com/Peltoche/lsd/releases/download/0.16.0/lsd-musl_0.16.0_amd64.deb \
  && dpkg -i bat_0.11.0_amd64.deb \
  && dpkg -i lsd-musl_0.16.0_amd64.deb \
  && rm bat_0.11.0_amd64.deb lsd-musl_0.16.0_amd64.deb

# Install Docker for docker in docker
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install git town
ENV GIT_TOWN_VERSION 7.2.1
RUN curl -ksSL "https://github.com/Originate/git-town/releases/download/v${GIT_TOWN_VERSION}/git-town-amd64.deb" -o /tmp/git-town-amd64.deb \
  && dpkg -i /tmp/git-town-amd64.deb

# Install libraries required for compiling Python 
RUN apt-get update \
  && apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git \
  && rm -rf /var/lib/apt/lists/*
USER ${DEV_USER}
ENV HOME /home/${DEV_USER}

RUN mkdir /home/${DEV_USER}/scripts
#ADD resources/two_line_prompt.sh /home/${DEV_USER}/scripts/two_line_prompt.sh

#RUN echo "source /home/${DEV_USER}/scripts/two_line_prompt.sh" >> /home/${DEV_USER}/.bashrc
#WORKDIR /home/${DEV_USER}

#ADD resources/start-dev-env.sh /home/${DEV_USER}/scripts/

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
#RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
#RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
#RUN echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
RUN echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"
ENV HOME /home/${DEV_USER}
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
ARG PYTHON_VERSION=3.8.0
RUN pyenv install ${PYTHON_VERSION}
#RUN pyenv install 3.8-dev 
#RUN pyenv install 3.9-dev 
#RUN pyenv install 3.6.9
RUN pyenv global ${PYTHON_VERSION}
RUN pyenv rehash

ENV DEBIAN_FRONTEND=dialog
