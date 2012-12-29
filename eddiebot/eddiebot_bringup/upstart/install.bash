#!/bin/bash

# Run this as root, from the directory containing it!
#
# USAGE: sudo ./install.bash
#  or
# sudo ./install.bash usb0
#  or
# sudo ./install.bash usb0 fuerte
#
# where usb0 is whatever network interface you want to set the robot
# up for.
# and fuerte is the specified version of ROS to use.
# Default is the latest installed.

interface=$(iwconfig 2>/dev/null | awk '{print $1}' | head -n1)

stackPath=/home/paralax2/fuerte_workspace/sandbox/eddiebot/eddiebot_bringup/upstart
#stackPath=./

if [ $# -gt 0 ]; then
    if [ "$1" != "" ]; then
        interface=$1
    fi
fi

release=$(ls /opt/ros/ | tail -n1)

if [ $# -gt 1 ]; then
    if [ "$2" != "" ]; then
        release=$2
    fi
fi


source /opt/ros/$release/setup.bash
OLD_DIR=$(pwd)
#cd `rospack find eddiebot_bringup`/upstart

# checks if eddiebot user+group exists, if it doesn't, then it creates a eddiebot daemon.

if ! grep "^eddiebot:" /etc/group >/dev/null 2>&1; then
    echo "Group eddiebot does not exist, creating."
    groupadd eddiebot
fi

if ! id -u eddiebot >/dev/null 2>&1; then
    echo "User eddiebot does not exist, creating and adding it to groups eddiebot and sudo."
    useradd -g eddiebot eddiebot
    usermod eddiebot -G sudo
    if [ ! -e /home/eddiebot ]; then
        echo "Eddiebot home directory was not created, creating."
        mkdir /home/eddiebot
        chown eddiebot:eddiebot /home/eddiebot
    fi
fi

cp $stackPath/52-eddiebot.rules /etc/udev/rules.d/

source /opt/ros/$release/setup.bash

echo "Installing using network interface $interface."

sed "s/eth1/$interface/g" < $stackPath/eddiebot-start | sed "s/fuerte/$release/"g > /usr/sbin/eddiebot-start
chmod +x /usr/sbin/eddiebot-start
sed "s/eth1/$interface/g" < $stackPath/eddiebot-stop | sed "s/fuerte/$release/"g > /usr/sbin/eddiebot-stop
chmod +x /usr/sbin/eddiebot-stop
sed "s/eth1/$interface/g" < $stackPath/eddiebot.conf > /etc/init/eddiebot.conf

# Copy files into /etc/ros/$release/eddiebot
mkdir -p /etc/ros
mkdir -p /etc/ros/$release
cat $stackPath/eddiebot.launch > /etc/ros/$release/eddiebot.launch

echo ". /opt/ros/$release/setup.bash;" > /etc/ros/setup.bash

cd $OLD_DIR
