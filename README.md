# Security-Automation-Stack
Capstone Project for Georgia Tech Master's in Cybersecurity

Containerized open-source stack

![image](https://github.com/zengrotrust/Security-Automation-Stack/assets/19690744/8c4a7061-8cf1-4eaf-a529-59326bb88646)

Increase max_map_count on your host (Linux)
Wazuh indexer creates many memory-mapped areas. So you need to set the kernel to give a process at least 262,144 memory-mapped areas.

Increase max_map_count on your Docker host:

`sysctl -w vm.max_map_count=262144`

Update the vm.max_map_count setting in `/etc/sysctl.conf` to set this value permanently. To verify after rebooting, run `sysctl vm.max_map_count`.

Warning If you don’t set the max_map_count on your host, the Wazuh, TheHive, and Shuffle indexers will NOT work properly.

Use install.sh script for auto-installation.

# 1. Clone the Wazuh repository to your home directory:
### $ cd
### $ sudo git clone https://github.com/wazuh/wazuh-docker.git -b v4.4.4

# 2. Clone the Shuffle repository to your home directory:
### $ sudo git clone https://github.com/Shuffle/Shuffle

# 3. Generate the Wazuh certificates:
### $ cd wazuh-docker/single-node
### $ sudo docker compose -f generate-indexer-certs.yml run --rm generator

# 4. Fix prerequisites for the Opensearch database
### $ cd
### $ cd Shuffle
### $ sudo mkdir shuffle-database
### $ sudo chown -R 1000:1000 shuffle-database

# 5. Clone this repository
### $cd
### $sudo git clone https://github.com/zengrotrust/Security-Automation-Stack

# 6. Replace all "/home/ubuntu" with your home directory in docker-compose.yml and .env

# 7. Run docker compose
### $ sudo docker compose up -d

# 8. Alternatively, you can deploy a stack via the Portainer GUI
### Make sure you load variables from .env file and change .env to stack.env

![image](https://github.com/zengrotrust/Security-Automation-Stack/assets/19690744/37db88c2-4ece-4aa3-aeca-b3673b1154cb)

