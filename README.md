# Suivi intermittence

Un petit outil gratuit pour suivre ses contrats, ses heures et ses revenus quand on est intermittent du spectacle. Il fonctionne dans le navigateur, sans compte et sans serveur : **vos données restent sur votre appareil**.

> Outil indicatif et non officiel. Vérifiez toujours vos chiffres auprès de France Travail et de Congés Spectacles.

## Ce que l’outil permet

- Enregistrer vos **engagements** : employeur, spectacle, lieu, dates, heures, brut, net social, net imposable, montant avant impôt et net payé.
- Enregistrer vos **versements France Travail** et vos **Congés Spectacles**.
- Suivre vos heures par rapport au **seuil de 507 h**, sur votre période de référence (à partir de votre date anniversaire, à renseigner dans l’outil).
- Voir un **récapitulatif du mois** (total des heures et du brut), utile pour l’actualisation mensuelle, avec des flèches pour revenir aux mois précédents.
- Être prévenu des engagements passés qui ne sont **pas encore marqués « payés »**.
- Consulter un **calendrier** et des **statistiques** (par mois, par année, par employeur).
- Filtrer par employeur, spectacle, type ou dates.
- Accéder au simulateur officiel de France Travail pour estimer votre futur taux.
- Choisir un mode clair ou sombre.

## Utilisation

Ouvrez simplement le lien de l’application dans votre navigateur. Elle fonctionne aussi **sans connexion** une fois chargée.

**Installer l’application** (facultatif) :

- Sur ordinateur, dans Chrome, Edge ou Brave : cliquez sur l’icône d’installation dans la barre d’adresse.
- Sur Android (Chrome) : menu, puis « Installer l’application ».
- Sur iPhone (Safari) : bouton Partager, puis « Sur l’écran d’accueil ».
- Firefox et les navigateurs qui en dérivent ne proposent pas cette installation sur ordinateur. L’application fonctionne très bien dans un onglet.

## Vos données

Tout est enregistré **dans votre navigateur**, sur l’appareil que vous utilisez. Rien n’est envoyé sur Internet.

Cela a deux conséquences :

- Chaque appareil, chaque navigateur et chaque copie installée a ses **propres données**. Elles ne se retrouvent pas automatiquement ailleurs.
- Si vous videz les données du navigateur, **elles sont effacées**.

Pensez donc à utiliser **« Exporter »** de temps en temps pour garder une sauvegarde. Le bouton **« Importer »** permet de la recharger, ou de transférer vos données vers un autre appareil.

## Importer un tableur existant

Le bouton **« Importer un tableur »** lit les fichiers **Excel (.xlsx)**, **LibreOffice (.ods)** et **CSV**. Vous indiquez quelle colonne correspond à quoi, vous vérifiez un aperçu, puis vous importez. Rien n’est ajouté avant votre confirmation, et ce qui existe déjà n’est pas importé deux fois.

Pour un ancien .xls ou un fichier Numbers, enregistrez-le d’abord en .xlsx, .ods ou CSV.

## Mettre l’application en ligne (pour la personne qui la publie)

Le dossier contient tout ce qu’il faut : `index.html`, `manifest.webmanifest`, `sw.js` et les quatre icônes `.png`. Il suffit de les déposer ensemble sur un hébergement de pages statiques, par exemple **GitHub Pages** : créez un dépôt, ajoutez les fichiers, puis activez « Pages » dans les réglages du dépôt.

Pour publier une mise à jour, remplacez `index.html`, puis changez le numéro de version en haut de `sw.js` (`suivi-v1` devient `suivi-v2`) si vous avez aussi modifié les icônes ou le manifeste.

## Un problème, une remarque ?

Une adresse de contact figure en bas de l’application.
