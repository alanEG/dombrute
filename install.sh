#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run with sudo"
    exit 1
fi

# Download Chrome installer
echo "Downloading Chrome installer..."
wget "https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_103.0.5060.134-1_amd64.deb" \
    -O /tmp/google-chrome-stable_current_amd64.deb

# Install Chrome
echo "Starting install Chromium browser..."
dpkg -i /tmp/google-chrome-stable_current_amd64.deb

# Fix any broken dependencies
apt --fix-broken install

# Download and install ChromeDriver
echo "Downloading ChromeDriver..."
current_path=`pwd`
wget https://chromedriver.storage.googleapis.com/103.0.5060.134/chromedriver_linux64.zip \
    -O /tmp/chromedriver_linux64.zip

cd /tmp/;unzip chromedriver_linux64.zip
cp /tmp/chromedriver ${current_path}

# Install mitmproxy using pip3
echo "Installing mitmproxy..."
pip3 install mitmproxy

# Remove the files
rm /tmp/google-chrome-stable_current_amd64.deb
rm /tmp/chromedriver_linux64.zip