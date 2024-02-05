# Le pilotage de l'inclusion

## Démarrer le projet

1. `source .venv/bin/activate`
2. `python manage.py runserver`

## Acces admin et DB

Pour l'accès à l'admin et pour récupérer la db (en sqlite3 pour l'instant), demander directement au patron

## ToDo

- Changer slug admin et mettre la var du slug dans constante .env (mais ça marche pas !?)
- Dockeriser la db postgres
- Passer la db en postgres (grace à la dockerisation)
- Créer le role pour les users aux droits limités dans l'admin
- Greffer Easy MDE sur le description.TextField
- Réintégrer les `<iframe>` metabase directement dans le site, sans passer par le C1
- Créer une instance CC et héberger le site
- Créer une instance CC pour les recettes jetable ou la demo
- Créer le nécessaire pour un déploiement auto (via cmd Makefile ?)
