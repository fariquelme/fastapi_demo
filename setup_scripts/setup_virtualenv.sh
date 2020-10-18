#!/bin/bash

if [ "$#" -eq 2 ]
 then
        PYTHON_VERSION=$1
        VIRTUALENV_NAME=$2
else
        echo 'No arguments passed, using default values: python 3.8.3 and virtualenv name yolodemo \nValid arguments example:  sh setup_virtualenv.sh 3.8.3 yolodemo'
        PYTHON_VERSION=3.8.3
        VIRTUALENV_NAME=yolodemo
fi

# Setup virtualenv manager (pyenv)
# install pyenv system dependencies
sudo apt update ; sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git 

# Pull pyenv-installer script and run
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# eddit .bashrc to enable pyenv on initialization
echo 'export PATH="/home/$USER/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# activate pyenv
export PATH="/home/$USER/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# print python version to be installed and virutalenv name
echo '=============== Pyenv Setup ==============='
echo "Python Version: $PYTHON_VERSION"
echo "Virtualenv Name: $VIRTUALENV_NAME"
echo '==========================================='

# Install new python version
pyenv install $PYTHON_VERSION

# Create virtualenv
pyenv virtualenv $PYTHON_VERSION $VIRTUALENV_NAME

# Activate created virtualenv
pyenv activate $VIRTUALENV_NAME
echo 'pyenv activate $VIRTUALENV_NAME' >> ~/.bashrc

# Install model python packages
pip install -r ../requirements.txt

# Install api python packages
pip install -r ../api/requirements.txt

# Install system packages

# Copy defualt env variables (includes default reddis password)
cp ../.env.example ../.env




tput setaf 2; echo 'done'; tput sgr0;
