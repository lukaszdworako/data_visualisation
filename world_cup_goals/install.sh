#!/usr/bin/env bash

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo osx
elif [[ "$OSTYPE" == "msys" ]]; then
    echo Cannot run script on windows system
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
    set -x
    sudo add-apt-repository ppa:jonathonf/python-3
    sudo apt-get update
    sudo apt-get install python3
    pip install selenium
    pip install bs4
fi