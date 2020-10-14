# Projet 11 [![Build Status](https://travis-ci.com/Tony380/Projet11.svg?branch=master)](https://travis-ci.com/Tony380/Projet11)
Améliorez un projet existant en Python

## Cadre du projet
Ce projet revient sur le projet 8, qui consistait en la création d'une application web
en utilisant le framework Django.

Ici, le but est de lui apporter des améliorations et des ajouts.

###Améliorations apportées:

-	Une photo de profil par défaut lorsqu’un utilisateur créé son compte
-	La possibilité de changer cette photo par la suite
-	La modification des données personnelles (adresse mail, nom d’utilisateur, etc…)
-	La modification du mot de passe
-	La suppression du compte

Les tests relatifs à ces améliorations ont été ajoutés.

###Pour tester l'application :
-   coverage run --source='.' manage.py test && coverage html && coverage report -m
