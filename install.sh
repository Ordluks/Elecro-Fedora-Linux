#!/bin/bash

echo "
This script will setup Electro Fedora configuration on your Fedora Linux system.
We will start installation after you entering sudo password.

Tip: You better to make system upgrade before continue

GitHub source - https://github.com/Ordluks/Elecro-Fedora-Linux
"

logs_dir=logs

if [ ! -d $logs_dir ]; then
  mkdir $logs_dir
fi

sudo python3 ./installer/main.py $HOME