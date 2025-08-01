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

## Dernières Actions
- **Gestion des Utilisateurs :**
    - Amélioration de l'interface d'administration des utilisateurs : les opérations d'ajout et de modification se font désormais sans rechargement de page, offrant une expérience utilisateur plus fluide.
    - Refonte de la page de connexion (`users/login.html`) : mise à jour du design, ajout d'un lien "Mot de passe oublié", et implémentation de la fonctionnalité "Se souvenir de moi".
    - Correction des problèmes de déconnexion (passage de GET à POST pour le formulaire de déconnexion) et d'affichage des modales JavaScript sur la page d'administration (inclusion du bloc `extra_js` dans `base.html`).
    - Correction des erreurs `NoReverseMatch` et `SyntaxError` liées aux namespaces d'URL et aux templates JavaScript.
    - Ajout de logs pour le diagnostic de l'envoi d'e-mails de bienvenue.
- **Gestion des Cours :**
    - Création de l'application `courses` et ajout à `INSTALLED_APPS`.
    - Définition des modèles `Course`, `Module`, et `Ressource` dans `courses/models.py`.
    - Création et application des migrations pour les nouveaux modèles.
    - Enregistrement des modèles `Course`, `Module`, `Ressource` dans `courses/admin.py` pour l'interface d'administration par défaut.
    - Intégration de la gestion des cours dans l'interface d'administration personnalisée :
        - Ajout de la vue `course_management_page` dans `administration/views.py` et son URL associée.
        - Création du template `administration/course_management.html` pour lister les cours.
        - Création du `CourseForm` dans `courses/forms.py`.
        - Implémentation des vues d'API (`create_course`, `update_course`, `delete_course`, `course_detail`) dans `administration/views.py` et leurs URLs.
        - Ajout de la modale et du JavaScript pour le CRUD dynamique des cours dans `course_management.html`.
        - Ajout d'un lien "Cours" dans la barre de navigation pour les administrateurs.
        - Création de la page de détail d'un cours (`/administration/cours/<int:course_id>/`) avec la vue `course_detail_page` et le template `course_detail_page.html`.
        - Déplacement des vues API des modules et ressources vers `courses/views.py` et création de `courses/urls.py`.
        - Mise à jour des décorateurs (`module_owner_or_admin_required`, `ressource_owner_or_admin_required`) pour gérer les permissions des enseignants et administrateurs.
        - Correction des URLs JavaScript dans `administration/course_detail_page.html` pour pointer vers les nouvelles API de `courses`.
        - Mise à jour du tableau de bord enseignant (`users/dashboard_enseignant.html`) pour permettre le CRUD de leurs cours.
        - Mise à jour du tableau de bord étudiant (`users/dashboard_etudiant.html`) pour lister les cours et gérer l'inscription/désinscription.
        - Création de la vue et du template pour le détail du cours étudiant (`users/views.py`, `users/templates/users/course_detail_student.html`).
        - Correction des erreurs JavaScript (`TypeError`, `SyntaxError`) et `NoReverseMatch` liées aux mises à jour dynamiques et aux URLs.

## Prochaines Étapes
1.  **Améliorations de l'Expérience Utilisateur (UX) :**
    *   **Feedback Visuel :** Remplacer les `alert()` JavaScript par des messages de succès/erreur plus élégants (par exemple, des toasts Bootstrap ou des messages Django).
    *   **Indicateurs de Chargement :** Ajouter des indicateurs visuels (spinners) pour toutes les opérations AJAX afin d'informer l'utilisateur que l'action est en cours.
    *   **Validation Côté Client :** Implémenter une validation JavaScript plus robuste pour les formulaires des modales afin de fournir un feedback instantané avant l'envoi au serveur.
2.  **Gestion des Inscriptions (Admin/Enseignant) :**
    *   Permettre aux administrateurs et aux enseignants de voir la liste des étudiants inscrits à un cours spécifique.
    *   Ajouter la possibilité pour les administrateurs/enseignants d'inscrire ou de désinscrire manuellement des étudiants à un cours.
3.  **Tests et Préparation au Déploiement :**
    *   **Tests Automatisés :** Écrire des tests unitaires et d'intégration pour les fonctionnalités critiques (modèles, formulaires, vues, API).
    *   **Configuration de Déploiement :** Préparer le projet pour un environnement de production (gestion des fichiers statiques et médias, configuration de la base de données, sécurité).