### RestApi Django
## L’objectif de ce travail est : 
- Réalisation d’interface en utilisant le système de template de Django, 
- Mise en place d’une API REST avec Django pour l’application en React.js,
- Implémenter une authentification par jeton (Token) avec Django, 
- Communication avec une API REST.
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
![01](https://user-images.githubusercontent.com/75283741/147282154-fa864add-eec4-420c-9e43-7580fc65d04a.PNG)
3. Page de gestion des utilisateurs :
- Cette page contient une vue pour tous les locateur et locataires avec un bouton pour supprimer et réinitialiser le mot de passe de chaque  utilisateur.
- Bouton pour filtrer les utilisateurs selon leur profil.
- Bouton Pour ajouter un nouveau utilisateur.
![02](https://user-images.githubusercontent.com/75283741/147282157-cacea932-03d9-4a81-8500-e365f75c5379.PNG)
4. Page d’ajouter un utilisateur :
![03](https://user-images.githubusercontent.com/75283741/147282159-b2a5ce26-bf74-4034-9829-99f5d170e7a4.PNG)
- Il faut remplir tous les champs et s’assurer que les mots de passe soient identiques et que l’adresse e-mail n’existe pas.
![04](https://user-images.githubusercontent.com/75283741/147282160-96294d39-0e10-465f-8b97-b18f8faad3a3.PNG)
![05](https://user-images.githubusercontent.com/75283741/147282161-41d7e4d1-3fd4-44df-a9f2-34ebe1aa0348.PNG)
6. Page de réinitialisation du mot de passe :
![06](https://user-images.githubusercontent.com/75283741/147282164-0c869e42-261b-4877-8c7c-e1909019ada0.PNG)
- Il faut que les deux champs soient identiques au risque d’avoir l’erreur en rouge.
![07](https://user-images.githubusercontent.com/75283741/147282165-c1c505c7-eea6-44c1-9d23-1f59b40a243f.PNG)
#### Statistiques :
1. Page des statistiques :
Page des statistiques, elle contient un conteneur; qui permet de lister quelques statistiques à parties de la base de données sur : 
- Les utilisateurs, 
- Les chambres, 
- Les réservations (avec statut), 
- Le bénéfice et montant reçu
![08](https://user-images.githubusercontent.com/75283741/147282166-c155c0b2-8388-435f-ae5e-621c7f4df8d0.PNG)
### Application pour l’API REST et Swagger (api)
####Les Entités 
1. Locateur/Locataire :
- Récupère un locateur spécifique (par son jeton, après  authentification) et permet également la modification.
![987](https://user-images.githubusercontent.com/75283741/147282175-bb7ac3e5-c116-4fa8-8a75-48110018633c.PNG)

2. Réservation :
- Récupère une chambre spécifique (ID) d’un certain locateur (par son  jeton, après authentification) et permet également la modification et  la suppression.
![33](https://user-images.githubusercontent.com/75283741/147282170-cecacc78-ceab-49a4-95ca-a0b606493165.PNG)

- Récupère une réservation spécifique (ID) d’un certain locateur ou  locataire (par son jeton, après authentification) et permet également  la modification et la suppression. Le statut ne peut être modifié que  par le locateur.
![22](https://user-images.githubusercontent.com/75283741/147282169-14956871-d1af-427d-afb1-db326bee3291.PNG)

3. Chambre :
- Récupère l’ensemble des chambres d’un certain locateur (par son  jeton, après authentification) et permet également d’en ajouter une  nouvelle.
![99](https://user-images.githubusercontent.com/75283741/147282171-471f90b3-78e5-462e-ae15-5c0a3fcaabf9.PNG)
- Récupère une chambre spécifique (ID) d’un certain locateur (par son  jeton, après authentification) et permet également la modification et  la suppression.
![Capture](https://user-images.githubusercontent.com/75283741/147282178-4cab6a51-8d40-4457-a464-749eecdd5ada.PNG)
4. Ville :
- Récupère l’ensemble des régions principales de la province de Québec.
![777](https://user-images.githubusercontent.com/75283741/147282172-f3bbffb3-bc9b-4869-b062-f3acfc8fbea5.PNG)
