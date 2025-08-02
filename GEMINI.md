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
- **Fonctionnalité 4 : Annonces et Communication - TERMINÉE**
    - **Annonces :**
        - **Partie Enseignant/Admin :** Création du modèle `Annonce`, intégration du CRUD dynamique dans l'interface d'administration des cours.
        - **Partie Étudiant :** Affichage des annonces sur la page de détail du cours.
    - **Messagerie Interne :**
        - Création de l'application `messaging`.
        - Définition des modèles `Conversation` et `Message`.
        - Création des vues de base (boîte de réception, détail de la conversation) et des templates associés.
        - Intégration d'un lien "Messagerie" dans la barre de navigation.
        - Ajout de boutons "Contacter" pour démarrer des conversations depuis les pages de détail des cours.
        - Ajout d'un compteur de messages non lus dans la barre de navigation.
        - Amélioration de l'interface de conversation avec des bulles de chat.
        - Possibilité de rechercher des utilisateurs pour démarrer une conversation.
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
    - Création d'un template tag pour compter les messages non lus.
    - Mise à jour de la vue `conversation_detail` pour marquer les messages comme lus.
    - Amélioration de l'interface de `conversation_detail.html` avec des bulles de chat et un défilement automatique.
    - Ajout d'une vue d'API `search_users` dans `messaging/views.py` pour rechercher des utilisateurs.
    - Ajout de l'URL correspondante dans `messaging/urls.py`.
    - Intégration d'un champ de recherche et affichage des résultats dans `inbox.html`.
- **Améliorations de l'Expérience Utilisateur (UX) :**
    - **Feedback Visuel :** Remplacement des `alert()` JavaScript par des messages de succès/erreur plus élégants (toasts Bootstrap ou messages Django) dans les vues et les templates JavaScript.
    - **Indicateurs de Chargement :** Ajout de spinners et de la logique de désactivation/réactivation des boutons pour les opérations AJAX dans `administration/course_management.html`, `administration/user_management.html`, `users/dashboard_enseignant.html`, et `users/dashboard_etudiant.html`.
    - **Validation Côté Client :** Implémentation d'une validation JavaScript plus robuste pour les formulaires des modales afin de fournir un feedback instantané avant l'envoi au serveur.

## Prochaines Étapes
1.  **Gestion du Profil (Étudiant/Enseignant) :**
    *   Consultation et mise à jour des informations personnelles.
2.  **Navigation et Accès aux Cours :**
    *   Recherche de cours par mots-clés.
3.  **Suivi de la Progression :**
    *   Suivi de la progression dans chaque cours (pour étudiants).
    *   Consultation de la progression des étudiants par cours et par activité (pour enseignants/admins).
4.  **Notifications :**
    *   Alertes pour les nouvelles annonces, devoirs, ou messages.
5.  **Gestion des Comptes Utilisateurs (Admin) :**
    *   Verrouillage des comptes.
6.  **Gestion des Cours et Catégories (Admin) :**
    *   Création et gestion des catégories de cours.
7.  **Paramètres Généraux de la Plateforme (Admin) :**
    *   Configuration du thème et de la personnalisation de la plateforme (logo ISTC, couleurs).
    *   Gestion des plugins/extensions.
8.  **Rapports et Statistiques (Admin/Enseignant) :**
    *   Génération de rapports de participation et de performance des étudiants.
    *   Tableau de bord global sur l'activité de la plateforme (nombre d'utilisateurs actifs, cours les plus populaires, etc.).
    *   Journaux d'audit et de logs.
9.  **Sauvegarde et Restauration :**
    *   Outils de planification et d'exécution des sauvegardes de données.
10. **Maintenance :**
    *   Gestion des mises à jour.
11. **Interaction et Collaboration :**
    *   Accès à des classes virtuelles ou visioconférences (intégration).
