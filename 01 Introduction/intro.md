#Particularités de Python :
    * syntaxe simplifiée ; la simplification de la syntaxe est « compensée » par un rigueur dans l’indentation ; ce qui oblige à écrire des lignes de code propres,
    * typage dynamique ; en plus du confort, cette particularité permet la métaprogrammation et le réflexivité (métaprogrammation : programmes qui manipulent des données décrivant elles-mêmes des programmes – réflexivité : capacité d’un programme à examiner/modifier ses propres structures internes. Ces deux caractéristiques dans le cadre de programmes auto-modifiants,
    * modulable : les fonctions intégrées au langage sont relativement peu nombreuses, les autres sont regroupées dans des fichiers séparés qu’on appelle « modules ».

Exemple de module : le module « random ».
Il faudra l’appeler grâce à la syntaxe « from random import * » ; ce qui donnera l’accès à toute une série de fonctions liées à la génération aléatoire de données ;
Un aperçu :
    * randint(a,b) : Donne un entier choisit au hasard entre a et b compris.
    * random() : Donne un flottant au hasard dans l'intervalle,
    * choice(liste) : Choisit un élément au hasard dans une liste,
    * shuffle(liste) : Mélange la liste sur place (c'est à dire qu'il modifie la liste d'origine).
    * ...

#Domaines :
    *éducation, de plus en plus de jeu de programmation, comme les Lego Mindstorm peuvent être programmés en Python
    *développement WEB : à l’aide du framework Django, plutôt orienté back-end
    *data-science : 
        -c’est un langage populaire dans le Big Data, car il est modulable, puissant et facile à écrire,
        -aussi populaire dans le domaine du machine learning,
        -c’est un langage de script, Python excelle dans la récupération de paramètres, le parsing d’un fichier, les petits scripts rapides, etc.
    *beaucoup de logiciels scientifiques utilisent Python, de même qu’une partie des logiciels de géolocalisation
    * …

#Environnement
Pour travailler avec Python 3, il faut utiliser un interpréteur ; on peut travailler dans un terminal ou télécharger l’interpréteur Python IDLE :
    *Pour lancer un fichier dans le terminal : ouvrez le terminal dans le dossier qui contient le fichier.py et taper « python3 nom_fichier.py »
    *Installer IDLE suivant les instructions qui correspondent à votre OS.
    
Pour ce qui concerne VS Code, j’utilise l’extension « Python (microsoft) ».

