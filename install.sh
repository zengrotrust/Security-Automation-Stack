# This auto-install script only works if your home dir is /home/ubuntu. Otherwise, replace /home/ubuntu to your home dir in docker-compose.yml and .env 
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# Optional volume for Portainer, Docker GUI Management
sudo docker volume create portainer_data
# Optional installation for Portainer, Docker GUI Management
sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:latest
cd
sudo git clone https://github.com/wazuh/wazuh-docker.git -b v4.4.4
sudo git clone https://github.com/Shuffle/Shuffle
cd wazuh-docker/single-node
sudo docker compose -f generate-indexer-certs.yml run --rm generator
cd ~/Shuffle
sudo mkdir shuffle-database
sudo chown -R 1000:1000 shuffle-database
cd
sudo git clone https://github.com/zengrotrust/Security-Automation-Stack
cd Security-Automation-Stack
sudo docker compose up -d
