# Le pilotage de l'inclusion

## Initialiser le projet

1. `make venv`
2. créer un fichier `.env` en utilisant le fichier `.env.template` (données disponibles dans bitwarden)
3. créer un fichier `.envrc.local` contenant au minimum le chemin vers le .venv (`source .venv/bin/activate`)
4. créer un superuser `python manage.py createsuperuser`
5. importer les fixtures des tableaux de bords `python manage.py loaddata "pilotage/fixtures/dashboard.json"`
6. construire le container docker `docker-compose build`


## Démarrer le projet

Démarrez les dépendances de développement avec la commande :
```sh
docker-compose up
```

Démarrer le serveur de développement avec la commande :

```sh
make runserver
```


## Lancer les tests
Le projet utilise [pytest](https://docs.pytest.org/).

Lancer le formatage du code :
```sh
make fix
```
