### RestApi Django
## L’objectif de ce travail est : 
- Réalisation d’interface en utilisant le système de template de Django, 
- Mise en place d’une API REST avec Django pour l’application en React.js,
- Implémenter une authentification par jeton (Token) avec Django, 
- Communication avec une API REST.

<b/ >

## Technologies utilisées : 
- Microsoft Visual Studio Code.
- Les différents packages nécessaires (Django, Django Rest Framework, Swagger).
- Pour l’aspect graphique; le Framework Twitter Bootstrap 5.
- Pour les icônes; Font Awsome.
- Environnement virtuel Python avec venv.

## Implémentation :
### Application pour l’interface d’administration (ui)
#### Gestion des utilisateurs :
1. Page d’accueil :
2. Page de gestion des utilisateurs :
- Cette page contient une vue pour tous les locateur et locataires avec un bouton pour supprimer et réinitialiser le mot de passe de chaque  utilisateur.
- Bouton pour filtrer les utilisateurs selon leur profil.
- Bouton Pour ajouter un nouveau utilisateur.
3. Page d’ajouter un utilisateur :
4. Page de réinitialisation du mot de passe
#### Statistiques :
1. Page des statistiques :
Page des statistiques, elle contient un conteneur; qui permet de lister quelques statistiques à parties de la base de données sur : 
- Les utilisateurs, 
- Les chambres, 
- Les réservations (avec statut), 
- Le bénéfice et montant reçu
### Application pour l’API REST et Swagger (api)
####Les Entités 
1. Locateur/Locataire :
- Récupère un locateur spécifique (par son jeton, après  authentification) et permet également la modification.

2. Réservation :
- Récupère une chambre spécifique (ID) d’un certain locateur (par son  jeton, après authentification) et permet également la modification et  la suppression
- Récupère une réservation spécifique (ID) d’un certain locateur ou  locataire (par son jeton, après authentification) et permet également  la modification et la suppression. Le statut ne peut être modifié que  par le locateur
3. Chambre :
- Récupère l’ensemble des chambres d’un certain locateur (par son  jeton, après authentification) et permet également d’en ajouter une  nouvelle.
- Récupère une chambre spécifique (ID) d’un certain locateur (par son  jeton, après authentification) et permet également la modification et  la suppression.
4. Ville :
- Récupère l’ensemble des régions principales de la province de Québec
