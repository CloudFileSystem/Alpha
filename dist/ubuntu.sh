#!/bin/bash

#
# install python setuptools
#
sudo apt-get -y install python-setuptools
sudo apt-get -y install python-pip
sudo apt-get -y install python-dev

#
# install pip
#
easy_install pip

#
# virtualenv & activate
#
pip install virtualenv
virtualenv .
source ./bin/activate


# vim: set nu ts=2 autoindent : #

