#!/bin/bash
# Update mininet

sudo apt-get update
sudo apt-get install python-pip python-dev build-essential
sudo apt-get install build-essential libpoppler-cpp-dev pkg-config
sudo pip install pdftotext
sudo pip install py-getch
sudo pip install "subprocess32>=3.2.6"
