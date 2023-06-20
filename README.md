# Security-Automation-Stack

# 1. Clone the Wazuh repository to your home directory:
### $ cd
### $ sudo git clone https://github.com/wazuh/wazuh-docker.git -b v4.4.4

# 2. Clone the Shuffle repository to your home directory:
### $ sudo git clone https://github.com/Shuffle/Shuffle

# 3. Generate the Wazuh certificates:
### $ cd wazuh-docker/single-node
### $ sudo docker-compose -f generate-indexer-certs.yml run --rm generator

# 4. Fix prerequisites for the Opensearch database
### $ cd
### $ cd Shuffle
### $ sudo mkdir shuffle-database
### $ sudo chown -R 1000:1000 shuffle-database

# 5. Download docker-compose.yml and .env, place them in the same directory

# 6. Replace all "/home/joey" with your home directory in docker-compose.yml and .env

# 6. Run docker compose
### $ sudo docker compose up -d

# 7. Alternatively, you can deploy a stack via the Portainer GUI
### Make sure you load variables from .env file and change .env to stack.env

![image](https://github.com/zengrotrust/Security-Automation-Stack/assets/19690744/37db88c2-4ece-4aa3-aeca-b3673b1154cb)

