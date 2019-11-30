FROM debian:buster-slim
LABEL MAINTAINER $(MAINTAINER)

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# This Dockerfile adds a non-root 'vscode' user with sudo access. However, for Linux,
# this user's GID/UID must match your local user UID/GID to avoid permission issues
# with bind mounts. Update USER_UID / USER_GID if yours is not 1000. See
# https://aka.ms/vscode-remote/containers/non-root-user for details.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Configure apt and install packages
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    #
    # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
    && apt-get -y install git iproute2 procps lsb-release \
    #
    # Install pylint
    && pip --disable-pip-version-check --no-cache-dir install pylint \
    #
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # [Optional] Add sudo support for the non-root user
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    #
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
  apt-utils \
  build-essential \
  curl \
  git \
  wget \
  && rm -rf /var/lib/apt/lists/*

# Install git town
ENV GIT_TOWN_VERSION 7.2.1
RUN curl -ksSL "https://github.com/Originate/git-town/releases/download/v${GIT_TOWN_VERSION}/git-town-amd64.deb" -o /tmp/git-town-amd64.deb \
  && dpkg -i /tmp/git-town-amd64.deb

USER ${USERNAME}
ENV HOME /home/${USERNAME}
RUN mkdir /home/${USERNAME}/scripts

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.8.0
RUN pyenv global 3.8.0
RUN pyenv rehash

ENV DEBIAN_FRONTEND=dialog
