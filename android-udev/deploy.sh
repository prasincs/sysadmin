#!/bin/bash
python gen_rules.py
sudo cp 51-android.rules /etc/udev/rules.d
