# Security-Automation-Stack
Capstone Project for Georgia Tech Master's in Cybersecurity

Containerized open-source stack in one docker compose file.

![image](https://github.com/zengrotrust/Security-Automation-Stack/assets/19690744/8c4a7061-8cf1-4eaf-a529-59326bb88646)


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

# 7. Cortex
### $ sudo mkdir cortex
### $ cd cortex
### $ sudo touch application.conf

# 8. Run docker compose
### $ sudo docker compose up -d

# 9. Alternatively, you can deploy a stack via the Portainer GUI
### Make sure you load variables from .env file and change .env to stack.env

![image](https://github.com/zengrotrust/Security-Automation-Stack/assets/19690744/37db88c2-4ece-4aa3-aeca-b3673b1154cb)

