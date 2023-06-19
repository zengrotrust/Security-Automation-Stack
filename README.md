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
$ sudo chown -R 1000:1000 shuffle-database
# 5.Replace all "/home/joey" with your home directory in docker-compose.yml
