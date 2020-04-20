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

Pour toutes les systèmes d'exploitation, il existe un installeur qui permet l'installation rapide du package (dans le dossier ``` installer ```).

Le package est, par défaut, installé en tant qu'__utilisateur lambda__ (pas en _super utilisation_ ou _administrateur_). Il sera donc nécessaire pour la suite d'utiliser la ligne de commande adéquat.

Pour les systèmes __windows__, l'installer est le fichier se terminant par ``` *.bat ```
Pour les systèmes __linux__, l'installer est le fichier se terminant par ``` *.sh ```
Pour les systèmes __macOS__, l'installer est le fichier se terminant par ``` *.command ```


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

Pour tous les systèmes d'exploitation, il existe un script de lancement (dans le dossier ``` launcher ```). Ce launcher peut etre utilisé n'importe où dans l'OS.

Pour les systèmes __windows__, le launcher est le fichier se terminant par ``` *.bat ```
Pour les systèmes __linux__, le launcher est le fichier se terminant par ``` *.sh ```
Pour les systèmes __macOS__, le launcher est le fichier se terminant par ``` *.command ```

#### Cheers
Coded with :heartpulse:
