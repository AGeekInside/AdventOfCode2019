FROM debian:buster-slim
LABEL MAINTAINER $(MAINTAINER)

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# This Dockerfile adds a non-root 'vscode' user with sudo access. However, for Linux,
# this user's GID/UID must match your local user UID/GID to avoid permission issues
# with bind mounts. Update USER_UID / USER_GID if yours is not 1000. See
# https://aka.ms/vscode-remote/containers/non-root-user for details.
ARG USERNAME=vsonline
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN touch /in_root
RUN touch /home/${USERNAME}/in_home

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
