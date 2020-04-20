# Airtable Export Convertor

Script python pour convertir fichiers CSV exportés depuis Airtable

## Usage
### Installation

Avant tout utilisation, il est nécessaire d'installer le package :

```
$ python setup.py install --user
```
ou en tant que super - utilisateur (uniquement pour les machines __unix__):

```
> sudo python setup.py install
```

### Ligne de commande

Le script analyse les arguments en entrée. Pour l'exécution, la commande a utilisé est :

* ``` python -m airtor.cli {args} ``` pour l'installation en __--user__
* ``` airtable-convertor {args} ``` pour l'installation en __super utilisateur__

Les 4 arguments utilisables, dans la version actuelle, sont :

* `[-d / -data] filename.csv` : chemin vers le fichier de données

* `[-o / -output] filename.csv` : nom du fichier de sortie

* `[--delimiter ] ` : caractère délimiteur du CSV

* `[--linebreak ] ` : caractère de saut de ligne du CSV

Par exemple :
```
$ python -m airtor.cli -d data.csv -o output.csv

$ airtable-convertor -d data.csv
```

#### Cheers
Coded with :heartpulse:
