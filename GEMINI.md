# Journal de Progression du Projet E-ISTC

## Statut Actuel
- **Fonctionnalité 1 : Gestion des Utilisateurs et Authentification - TERMINÉE**
    - Interface d'administration des utilisateurs entièrement dynamique (CRUD sans rechargement de page).
    - Page de connexion améliorée (design, lien mot de passe oublié, "se souvenir de moi").
    - Correction des bugs de déconnexion et de chargement des scripts JS.
- **Fonctionnalité 2 : Gestion des Cours - TERMINÉE**
    - Création de l'application `courses`.
    - Définition des modèles `Course`, `Module`, `Ressource`.
    - Application des migrations.
    - Enregistrement des modèles dans l'interface d'administration Django par défaut.
    - Intégration de la gestion des cours dans l'interface d'administration personnalisée (`administration` app).
        - Page de liste des cours (`/administration/cours/`) avec affichage des cours.
        - CRUD dynamique des cours (ajout, modification, suppression sans rechargement de page).
        - Page de détail d'un cours (`/administration/cours/<id>/`) avec gestion dynamique des modules et ressources (CRUD).
    - **Vues pour les Enseignants :**
        - Tableau de bord enseignant (`/comptes/dashboard/enseignant/`) listant leurs cours.
        - Création, modification et suppression de leurs propres cours depuis le tableau de bord.
        - Accès à la page de détail de leurs cours pour gérer modules et ressources.
    - **Vues pour les Étudiants :**
        - Tableau de bord étudiant (`/comptes/dashboard/etudiant/`) listant tous les cours disponibles.
        - Fonctionnalité d'inscription et de désinscription aux cours.
        - Page de détail d'un cours (`/comptes/courses/<id>/`) pour les étudiants inscrits (lecture seule).
- **Fonctionnalité 3 : Gestion des Évaluations - TERMINÉE**
    - **Partie Enseignant/Admin :**
        - Création de l'application `evaluations` et de ses modèles (`Activite`, `Question`, `Choix`, `Soumission`, `Tentative`) basés sur le schéma SQL.
        - Intégration de la gestion des évaluations dans l'interface d'administration des cours (CRUD dynamique des activités).
        - Interface dédiée pour la gestion des questions et choix de quiz.
        - Mise en place de décorateurs de permission spécifiques (`activity_owner_or_admin_required`, `question_owner_or_admin_required`, `submission_owner_or_admin_required`).
        - **Notation des devoirs :** Interface pour les enseignants/admins pour noter les soumissions de devoirs.
    - **Partie Étudiant :**
        - Affichage des évaluations sur la page de détail du cours étudiant.
        - Soumission de devoirs : page dédiée avec formulaire de téléversement et gestion de la soumission unique.
        - Passage de quiz : interface pour répondre aux questions, calcul du score et enregistrement de la tentative.
        - Consultation des notes : page récapitulative des notes obtenues aux devoirs et quiz.
- **Fonctionnalité 4 : Annonces et Communication - EN COURS**
    - **Annonces :**
        - **Partie Enseignant/Admin :** Création du modèle `Annonce`, intégration du CRUD dynamique dans l'interface d'administration des cours.
        - **Partie Étudiant :** Affichage des annonces sur la page de détail du cours.
    - **Messagerie Interne :**
        - Création de l'application `messaging`.
        - Définition des modèles `Conversation` et `Message`.
        - Création des vues de base (boîte de réception, détail de la conversation) et des templates associés.
        - Intégration d'un lien "Messagerie" dans la barre de navigation.
        - Ajout de boutons "Contacter" pour démarrer des conversations depuis les pages de détail des cours.
- **Fonctionnalité 5 : Gestion des Inscriptions - TERMINÉE**
    - **Partie Étudiant :**
        - Inscription et désinscription autonomes depuis le tableau de bord.
    - **Partie Enseignant/Admin :**
        - Affichage de la liste des étudiants inscrits sur la page de détail du cours.
        - Retrait d'un étudiant d'un cours.
        - Inscription manuelle d'un ou plusieurs étudiants à un cours via une interface modale.

## Dernières Actions
- **Gestion des Inscriptions (Admin/Enseignant) :**
    - Ajout des vues d'API `list_enrollable_students` et `enroll_student` dans `courses/views.py`.
    - Ajout des URLs correspondantes dans `courses/urls.py`.
    - Ajout d'un bouton "Inscrire un étudiant" et d'une modale dans `administration/course_detail_page.html`.
    - Implémentation du JavaScript pour charger les étudiants non-inscrits et les inscrire de manière asynchrone.
- **Messagerie Interne :**
    - Création de l'application `messaging` (`python manage.py startapp messaging`).
    - Ajout de `messaging` à `INSTALLED_APPS`.
    - Définition des modèles `Conversation` et `Message` dans `messaging/models.py`.
    - Création et application des migrations.
    - Création des vues `inbox`, `conversation_detail`, et `new_conversation`.
    - Création des templates `inbox.html` et `conversation_detail.html`.
    - Ajout des URLs pour la messagerie.
    - Ajout d'un lien "Messagerie" dans la barre de navigation (`base.html`).
    - Ajout de boutons "Contacter" sur les pages de détail des cours.

## Prochaines Étapes
1.  **Améliorations de la Messagerie :**
    *   Afficher un indicateur de messages non lus.
    *   Permettre de rechercher des utilisateurs pour démarrer une conversation.
    *   Améliorer l'interface de la conversation (par exemple, avec des bulles de chat distinctes pour l'émetteur et le récepteur).
2.  **Améliorations de l'Expérience Utilisateur (UX) :**
    *   **Feedback Visuel :** Remplacer les `alert()` JavaScript par des messages de succès/erreur plus élégants (par exemple, des toasts Bootstrap ou des messages Django).
    *   **Indicateurs de Chargement :** Ajouter des indicateurs visuels (spinners) pour toutes les opérations AJAX afin d'informer l'utilisateur que l'action est en cours.
    *   **Validation Côté Client :** Implémenter une validation JavaScript plus robuste pour les formulaires des modales afin de fournir un feedback instantané avant l'envoi au serveur.
3.  **Tests et Préparation au Déploiement :**
    *   **Tests Automatisés :** Écrire des tests unitaires et d'intégration pour les fonctionnalités critiques (modèles, formulaires, vues, API).
    *   **Configuration de Déploiement :** Préparer le projet pour un environnement de production (gestion des fichiers statiques et médias, configuration de la base de données, sécurité).