# Projet: Data Pipline 
Le projet est structuré comme suivant:
```bash
|-- config
    |-- config.clinical_trials.toml
    |-- config.drug.toml
    |-- config.pubmed.toml
|-- dag
|--datasets
    |-- clinical_trials.csv
    |-- drug.csv
    |-- pubmed.csv
|--output
    |-- data.json
|--src
    |-- drug_reference.py
    |-- graph_data.py
    |-- load_data.py
    |-- utiles.py
|--poetry.lock
|--pyprject.toml
|--README.md
```

### dossier config
ce dossier contient les fichiers de configuration en format toml correspont à chaque dataset csv

Exemple du fichier toml:

```toml
[file]
description = "contient des publications scientifiques avec un titre (scientific_title), un id (id), un journal (journal) et une date (date)."
path = "datasets/clinical_trials.csv"

[fields]
  [fields.id]
  type = "object"

  [fields.title]
  type = "object"

  [fields.journal]
  type = "object"

  [fields.date]
  type = "date"
```

### datasets
ce dossier contient les datasets en format csv à traiter

### src
ce dossier contient les scripts python qui composent le job de data pipline.

- classe LoadData dans le script load_data.py pour lire et charger les fichiers csv
- classe GraphJson dans le script graph_data.py pour générer l'output json orienté graphe de liaison
- classe UtilsGraph dans le script utiles.py pour extraire le noeud (exemple journal) qui a le maximum de liens (exemple le journal qui mentionne le plus de médicaments différents)
- script drug_reference. qui utilise les fonctions dévelppées dans les classes LoadData et GraphJson pour traiter les fichiers scv et génèrer le graph en json dans le dossier output.

## Environnement virtuel:

l'environnement virtuel qui gère les librairies python nécessaires pur le projet est crée par l'outil poetry de python.
Les fichier pyprojet.toml et poetry.lock contient les noms, versions et liens des différentes librairies utilisées par le projet.
