sudo apt install -y linux-headers-$(uname -r) build-essential dkms git libelf-dev

sudo dkms status

sudo dkms remove -k 5.15.0-30-generic rtl88x2bu/5.8.7.1

sudo ~/Downloads/rtl88x2bu/deploy.sh