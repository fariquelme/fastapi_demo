#!/bin/bash
# Exit on error
set -e
# Setup server
# Create new sudo user to avoid using root
echo 'Creating sudo user'
echo 'Username:'
read USERNAME
sudo useradd -s /bin/bash -d /home/$USERNAME -m -G sudo $USERNAME
echo 'Please set the password for your new user:'
passwd $USERNAME

# Add swap partition if ram is low
echo 'Add Swap Partition ? (y/n):'
read ADD_SWAP
if [ $ADD_SWAP == 'y' ]
then
    echo "Adding swap partition..."
    echo 'Setting up 3GB sized partition for swap'
    # Allocate swwap file
    sudo fallocate -l 3G /swapfile
    sudo dd if=/dev/zero of=/swapfile bs=1024 count=3145728
    # Change swapfile permissions
    sudo chmod 600 /swapfile
    # make swap parittion
    sudo mkswap /swapfile
    # Activate swap
    sudo swapon /swapfile
    # Add entry to mount swap partition on boot
    sudo echo '/swapfile swap swap defaults 0 0' >> /etc/fstab
    sudo swapon --show
    sudo free -h
else
    echo "Skipping swap parition creation..."
fi

echo "Moving repo to new user\'s home dir (/home/$USERNAME/)"

current_dir=$(pwd)
parent_dir=$(dirname "$current_dir")
cp -r  $parent_dir /home/$USERNAME

rm -r $parent_dir

chown -R $USERNAME:$USERNAME /home/$USERNAME

cd /home/$USERNAME
su $USERNAME


tput setaf 2; echo 'done'; tput sgr0;
