# Cartage
Mini page "Cartage" Django réalisée dans le cadre de ma formation de CDA. Vous y trouverez un site (extrêmement) rudimentaire avec de l'authentification (non sécurisée), une navigation basique et un système de contacts / messagerie. 

L'idée derrière ce mini-projet de quelques jours était de s'appuyer sur un concept trouvé en groupe avec Yann Nivot, Benoît Hert, et Pierre Napoletano d'une application de covoiturage intelligent, regrouper des conducteurs expérimentés et des apprenants réalisant les mêmes trajets pour que l'apprennant fasse ses heures de conduite accompagnée, tandis que le conducteur expérimenté est légèrement rémunéré. Le développement a ensuité été réalisé en groupe avec Yann Nivot et Benoît Hert

## Installation
- Cloner ce repo via `git clone https://github.com/Eliott-Mischler/Cartage.git`
- Ouvrir le dossier du projet, se rendre dans mysite/
- Ouvrir l'invite de commande puis exécuter `python manage.py migrate`
- Exécuter `python manage.py runserver`
- Changer le dictionnaire DATABASES de settings.py pour modifier la connexion en BDD à souhait

## Pré-requis
- Python 3.9+
- MySQL installé localement, avec une instance locale sur le port 3306 (par défaut, USER: formateur PASSWORD : formateur)
- librairies `Django`, `mysqlclient`
