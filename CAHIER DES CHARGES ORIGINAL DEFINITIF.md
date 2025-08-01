***CAHIER DES CHARGES ORIGINAL***

***PROJET : MISE EN PLACE D’UNE PLATEFORME DE E-LEARNING AU SEIN DE ISTC (E-ISTC)***

***Introduction***

` `Le e-learning désigne l'ensemble des solutions permettant d'assurer une formation à distance via des moyens électroniques. L'ISTC souhaite mettre en œuvre une plateforme de e-learning afin de moderniser son dispositif pédagogique, de garantir une continuité d'apprentissage et de permettre un meilleur accès aux contenus éducatifs pour les étudiants et enseignants.

***I. Présentation de l’existant Actuellement***

L’ISTC ne dispose pas d’une plateforme dédiée à l’enseignement en ligne. L’enseignement repose principalement sur des cours en présentiel, avec une diffusion des supports pédagogiques de manière informelle (impression papier ou groupes WhatsApp). Il n'existe pas de système intégré de gestion des cours, des inscriptions ou des évaluations numériques.

***II. Critiques et limites de l’existant***  

-Absence de continuité pédagogique en cas d’empêchement physique ou de crise sanitaire. 

\- Aucune centralisation des cours, des ressources et des notes. 

\- Faible interactivité et collaboration entre enseignants et étudiants à distance.

` `- Manque de suivi personnalisé des étudiants. 

\- Perte ou éparpillement des contenus pédagogiques.

` `- Absence d’outils statistiques ou de reporting.

***III. Problématiques et description de la demande*** 

***III-1) Problématique***

` `Comment mettre en place une plateforme de e-learning moderne, collaborative et évolutive permettant à l’ISTC de dispenser un enseignement de qualité à distance tout en répondant aux besoins techniques, pédagogiques et administratifs ? 

***III-2) Description des besoins***

` `- Gestion des utilisateurs (étudiants, enseignants, administrateurs) 

\- Création, diffusion et organisation des cours 

\- Téléversement de ressources multimédias 

\- Suivi des étudiants et notation des devoirs

\- Évaluations en ligne (quiz, devoirs) :

\- Forums, messagerie interne, visioconférences 

\- Interface intuitive et responsive 

\- Gestion de la sécurité, des sauvegardes et des statistiques

**a- *Besoins Fonctionnels***

La plateforme E-ISTC sera structurée autour de trois rôles utilisateurs principaux : **Administrateur**, **Enseignant** et **Étudiant**, chacun avec des fonctionnalités spécifiques.

**- Fonctionnalités pour les Étudiants**

- **Accès et Authentification :**
  - *Connexion sécurisée avec identifiant et mot de passe. (propre à chaque étudiant durant toute sa période de formation sur la plateforme E-ISTC).*
  - *Réinitialisation du mot de passe.*
- **Gestion du Profil :**
  - *Consultation et mise à jour des informations personnelles.*
- **Navigation et Accès aux Cours :**
  - *Tableau de bord personnalisé avec les cours inscrits.*
  - *Recherche par mot clés et inscription aux cours disponibles.*
  - *Accès aux ressources de cours (PDF, vidéos, présentations, liens externes).*
  - *Suivi de la progression dans chaque cours.*
- **Interaction et Collaboration :**
  - *Forums de discussion dédiés à chaque cours.*
  - *Messagerie interne avec les enseignants et autres étudiants du cours pour les critiques et suggestions.*
  - *Possibilité de soumettre des travaux.*
  - *Accès à des classes virtuelles ou visioconférences (intégration).*
- **Évaluations :**
  - *Participation à des quiz et examens en ligne.*
  - *Consultation des notes et retours des enseignants.*
- **Notifications :**
  - *Alertes pour les nouvelles annonces, devoirs, ou messages.*
- **Fonctionnalités pour les Enseignants**
- **Accès et Authentification :**
  - *Connexion sécurisée.*
- **Gestion des Cours :**
  - *Création, modification et suppression de cours.*
  - *Organisation des contenus par modules/sections.*
  - *Téléchargement et gestion de divers formats de ressources (vidéos, audio, documents, liens).*
  - *Création d'activités (devoirs, quiz, sondages).*
  - *Gestion des inscriptions (ajout/suppression manuelle d'étudiants, si besoin).*
- **Suivi des Étudiants :**
  - *Consultation de la progression des étudiants par cours et par activité.*
  - *Notation des devoirs et publication des résultats.*
  - *Envoi de retours individuels aux étudiants.*
- **Communication :**
  - *Annonces générales pour un cours.*
  - *Participation aux forums de discussion.*
  - *Messagerie interne avec les étudiants.*
  - *Planification et animation de sessions de classe virtuelle.*
- **Rapports :**
  - *Génération de rapports de participation et de performance des étudiants.*
- ` `**Fonctionnalités pour les Administrateurs**
- **Gestion des Utilisateurs :**
  - *Création, modification, suppression d'utilisateurs (étudiants, enseignants, autres admins).*
  - *Gestion des rôles et permissions.*
  - *Gestion des comptes utilisateurs (réinitialisation mot de passe, verrouillage).*
- **Gestion des Cours et Catégories :**
  - *Création et gestion des catégories de cours.*
  - *Assignation des enseignants aux cours.*
  - *Supervision des cours.*
- **Paramètres Généraux de la Plateforme :**
  - *Configuration du thème et de la personnalisation de la plateforme (logo ISTC, couleurs).*
  - *Gestion des plugins/extensions* 
  - *Configuration des paramètres de sécurité.*
- **Rapports et Statistiques :**
  - *Tableau de bord global sur l'activité de la plateforme (nombre d'utilisateurs actifs, cours les plus populaires, etc.).*
  - *Journaux d'audit et de logs.*
- **Sauvegarde et Restauration :**
  - *Outils de planification et d'exécution des sauvegardes de données.*
- **Maintenance :**

*Gestion des mises à jour*
### **. Choix Technologiques**
*La stack technologique a été spécifiquement choisie pour sa synergie et sa capacité à répondre aux exigences du projet :*

- **Framework Web : Django**
  - *Choisi pour son approche "batteries incluses" qui favorise un développement rapide, sécurisé et structuré. Django permettra de construire une application monolithique robuste, intégrant à la fois le back-end et le front-end.*
- **Base de Données : MySQL**
  - *Conservée pour sa performance, sa fiabilité et sa maturité pour la gestion des données relationnelles volumineuses. Django s'intègre parfaitement avec MySQL.*
- **Front end : Templates Django (HTML, CSS, JavaScript)**
  - *Le front-end sera rendu directement par Django. Nous utiliserons HTML, CSS, et JavaScript (avec le framework Bootstrap) pour créer une interface utilisateur intuitive et responsive, sans la complexité d'une Single Page Application (SPA) séparée.*

**IV. Déroulement du projet**

` `***IV-1) Planification*** 

Phase 1 : Analyse et Spécification (4 semaines) 

Phase 2 : Développement / Intégration (5 semaines)

` `Phase 3 : Tests et Recette (2 semaine)

` `Phase 4 : Formation et Déploiement (4 semaine)

` `***IV-2) Ressources humaines***

` `- Chef de projet (superviseur ISTC) 

\- Équipe de développement (UNIVERS BINAIRE SARL) 

\- Enseignants référents - Responsables pédagogiques 

\- Service informatique ISTC 

***IV-3) Coûts estimatifs***

Le projet repose idéalement sur une solution open source (développement personnalisé). Le coût estimé inclut : 

\- Infrastructure (hébergement, serveur)

` `- Développement / personnalisation 

\- Maintenance initiale et formation 

\- Coût total estimé : à définir selon la solution choisie.

***V. Livrables*** 

\- Plateforme e-learning fonctionnelle 

\- Documentation utilisateur et technique 

\- Guides de formation 

\- Rapports de tests 

\- Rapport de projet et cahier des charges finalisé 

***Conclusion***

