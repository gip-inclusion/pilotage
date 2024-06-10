# Le pilotage de l'inclusion

## Initialiser le projet

1. `make venv`
2. créer un fichier `.envrc.local` contenant au minimum le chemin vers le .venv : `echo "source .venv/bin/activate" >> .envrc.local`
3. créer un superuser `python manage.py createsuperuser`
4. importer les fixtures des tableaux de bords `python manage.py loaddata "pilotage/fixtures/dashboard.json"`
5. construire le container docker `docker-compose build`
6. Si vous souhaitez utiliser les tableaux de bord metabase de production, ajouter `METABASE_SECRET_KEY` à votre `.envrc.local`

## Démarrer le projet

Démarrez les dépendances de développement avec la commande :
```sh
docker-compose up
```

Démarrer le serveur de développement avec la commande :

```sh
make runserver
```


## Outils

Lancer le formatage du code :
```sh
make fix
```
