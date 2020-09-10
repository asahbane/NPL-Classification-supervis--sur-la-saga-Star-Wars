## Compte GitHub pour le travail collaboratif :

Pour bien commencer ce projet, envoyez nous vos identifiants aux deux adresses suivantes :

tiffany.cherchi@umontpellier.fr et florent.bascou@umontpellier.fr

Nous vous donnerons alors accès aux données ainsi qu'aux supports utiles au projet, disponibles ici :

https://github.com/tiffanycherchi/Project_2020_BC


## Application GitHub Desktop :

Maintenant, et sauf si vous êtes sous linux, téléchargez l'application :

https://desktop.github.com

Elle vous permettra de gérer vos fichiers via Git, et de régulièrement "pousser" toutes vos avancées.

L'objectif pour nous n'est absolument pas de contrôler tout votre travail, mais plutôt de vous aider à prendre de 'bonnes pratiques'.
Le fait de pousser régulièrement vous aidera à voir le travail avancer.


## Anaconda :

Si vous ne l'avez pas encore fait, téléchargez la distribution Anaconda :

https://www.anaconda.com/distribution/

Vous en aurez besoin pour traiter des documents de type notebook (.ipynb) ou python (.py).

Passons au travail !


# Classification de personnages dans la trilogie originale Star Wars

La saga Star Wars est constituée de 3 trilogies, qui font intervenir de nombreux personnages, que l'on peut distinguer selon leur espèce, leur genre, ou encore leur appartenance à un groupe. Pour chacun des trois épisodes de la trilogie originale, vous aurez pour données les dialogues ainsi que des caractéristiques concernant les personnages présents.

L'objectif de ce travail est de mettre en évidence les principaux indicateurs (âge, genre, champs lexicaux utilisés) qui influencent le nombre d'intervention et le temps de parole des personnages. On pourra en déduire si la répartition du temps de parole est équilibrée ou pas. Enfin, on essayera de répondre à la question suivante : d'après l'analyse des données de la première trilogie, aurait-on pu prédire que la personnage principale de la dernière trilogie était une femme ?

Mots clés : classification, analyse de texte, grande dimension, python (Scikit-learn, Matplotlib, Seaborn, Pandas, Numpy, ...).

## Pré-traitement des données

La première étape de ce projet sera de prendre en main les données (brutes) des scripts de la saga, et d'opérer les premiers traitements permettant de les transformer en données exploitables automatiquement.

## Traitement et visualisation des données

Une deuxième étape serait de choisir et représenter des indicateurs statistiques qui influencent le nombre d'intervention et le temps de parole des personnages. En particulier,  vous devrez analyser les données textuelles de dialogues pour créer certains de ces indicateurs.

## Choix de modèles

A partir des données, vous choisirez une ou des méthodes d'apprentissage statistique, afin de répondre à la problématique du projet. En particulier, vous justifierez le choix des méthodes sélectionnées, et détaillerez la comparaison de ces méthodes.

## Prédiction

Enfin, à partir de tout ce travail, on essayera de prédire si, d'après ces données, le personnage principale de la dernière trilogie aurait été une femme.
