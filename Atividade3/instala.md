curl -fsSL https://download.opensuse.org/repositories/security:zeek/Debian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
echo 'deb http://download.opensuse.org/repositories/security:/zeek/Debian_12/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list

sudo apt update

sudo apt install zeek-lts

echo "export PATH=$PATH:/opt/zeek/bin" >> ~/.bashrc

source ~/.bashrc
echo $PATH

which zeek
zeek --version
zeek --help


ip a

sudo nano /opt/zeek/etc/networks.cfg


