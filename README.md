# Hydroponie
Controle d'un système Hydroponie.

Le module central de contrôle du système est un Raspberry Pi modèle 3 B. Il est alimenté par une alimentation externe 5v 3A.
Un bus de communication CAN informe le module central des données mesurées par les différents capteurs.

## Installation du RaspberryPi
Réaliser un un update et un upgrade
```
sudo apt-get update && sudo apt-get upgrade -y
```

Installer can-utils
```
sudo apt-get install can-utils
```

Activer la creation du resau can0 a chaque boot en créant un fichier: /etc/systemd/network/80-can.network 
```
sudo nano /etc/systemd/network/80-can.network
```
Y ajouter le contenu suivant:
```
[Match]
Name=can0

[CAN]
BitRate=500K
```
Reactiver systemd-networkd
```
sudo systemctl restart systemd-networkd
sudo systemctl enable systemd-networkd
```
Vérifier que le reseau can0 est existe avec la commande:
```
ifconfig
```
Vérifier la réception de messages can:
```
candump can0
```

Installer git
```
sudo apt install git
```

Installer Docker
```
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker $USER
sudo reboot
```

Cloner le repo git
```
git clone https://github.com/gregoryvanko/Hydroponie.git Docker
```

Créer un fichier .env dans le répertoire Hydroponie avec le contenu suivant:
```
CLOUDFLARED_TOKEN=djyugricbd...
```

Créer et exécuter le container
```
docker compose up -d
```

## Mesure du niveau d'eau par ultrason
Pour calculer le pourcentage de volume d'eau, les distances entre le capteur à ultrason et le niveau d'eau le plus bas (SONAR_MAX) / le plus haut (SONAR_MIN) doivent etre définies dans le fichier NodeRed/Data/config.json:
```
{"SONAR_MIN":7,"SONAR_MAX":72}
```

## CloudFlared
Pour se connecter au Raspberry Pi depuis internet on va créer un tunnel via CloudFlare.

Il faut configurer un tunnel dans Claudflare et sauver le token communiqué par ClaudFlare dans le fichier .env à sauver sur le Raspberry PI.
```
CLOUDFLARED_TOKEN=djyugricbd...
```

## Le fichier .env a créer dans le dossier Hydroponie:
```
CLOUDFLARED_TOKEN=djyugricbd...
```

## Le fichier config.json:
```
{"SONAR_MIN":8,"SONAR_MAX":72}
```

# Update
Ajouter le package NodeRed à installer dans le fichier NodeRed/Configuration/dockerfile en y copiant la ligne suivante: 
```
RUN npm install xxx
```
