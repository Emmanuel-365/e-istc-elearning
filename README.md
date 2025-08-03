# E-ISTC: Plateforme de E-Learning

![E-ISTC Logo](e_istc/static/img/E-LEARNING%20(3).png) <!-- Assuming a logo exists at this path -->

## Table des Matières

1.  [Introduction](#introduction)
2.  [Fonctionnalités](#fonctionnalités)
    *   [Administrateur](#administrateur)
    *   [Enseignant](#enseignant)
    *   [Étudiant](#étudiant)
3.  [Technologies Utilisées](#technologies-utilisées)
4.  [Installation et Configuration](#installation-et-configuration)
    *   [Prérequis](#prérequis)
    *   [Étapes de Configuration](#étapes-de-configuration)
5.  [Lancer l'Application](#lancer-lapplication)
6.  [Exécuter les Tests](#exécuter-les-tests)
7.  [Commandes de Gestion Personnalisées](#commandes-de-gestion-personnalisées)
8.  [Conventions de Développement](#conventions-de-développement)
9.  [Licence](#licence)

---

## Introduction

E-ISTC est une plateforme de e-learning monolithique développée avec le framework web Django. Elle est conçue pour moderniser le dispositif pédagogique de l'ISTC, assurer une continuité d'apprentissage et faciliter l'accès aux contenus éducatifs pour trois rôles d'utilisateurs principaux : les **Administrateurs**, les **Enseignants**, et les **Étudiants**. La plateforme gère la création de cours, la diffusion de contenu, les évaluations et la communication interne.

---

## Fonctionnalités

La plateforme offre un ensemble riche de fonctionnalités adaptées à chaque rôle utilisateur :

### Administrateur

*   **Gestion des Utilisateurs :** Création, modification, suppression, et gestion des rôles/permissions (Admin, Enseignant, Étudiant). Verrouillage et déverrouillage des comptes utilisateurs.
*   **Gestion des Cours et Catégories :** Création, modification, suppression de cours et de catégories. Assignation des enseignants aux cours et supervision générale.
*   **Paramètres Généraux de la Plateforme :** Configuration du thème, personnalisation (logo, couleurs), et gestion des paramètres de sécurité.
*   **Rapports et Statistiques :** Tableau de bord global sur l'activité de la plateforme (utilisateurs actifs, cours populaires, etc.). Génération de rapports de participation et de performance.
*   **Journaux d'Audit :** Interface dédiée pour consulter les logs d'administration.
*   **Sauvegarde et Restauration :** Outils pour la planification et l'exécution des sauvegardes de données.
*   **Maintenance :** Commandes pour l'application des migrations et la collecte des fichiers statiques.

### Enseignant

*   **Gestion des Cours :** Création, modification, et suppression de leurs propres cours. Organisation des contenus par modules et sections. Téléchargement et gestion de ressources multimédias (vidéos, documents, liens).
*   **Gestion des Évaluations :** Création d'activités (devoirs, quiz, sondages). Interface pour la gestion des questions et choix de quiz. Notation des devoirs soumis par les étudiants.
*   **Suivi des Étudiants :** Consultation de la progression des étudiants par cours et par activité. Envoi de retours individuels.
*   **Communication :** Publication d'annonces générales pour un cours. Participation aux forums de discussion. Messagerie interne avec les étudiants. Planification et animation de sessions de classe virtuelle (via lien externe).
*   **Gestion des Inscriptions :** Affichage de la liste des étudiants inscrits, retrait d'étudiants, et inscription manuelle.

### Étudiant

*   **Accès et Authentification :** Connexion sécurisée (identifiant, mot de passe, matricule/email). Réinitialisation du mot de passe.
*   **Gestion du Profil :** Consultation et mise à jour des informations personnelles.
*   **Navigation et Accès aux Cours :** Tableau de bord personnalisé avec les cours inscrits. Recherche de cours par mots-clés. Accès aux ressources de cours (PDF, vidéos, présentations, liens externes). Suivi de la progression dans chaque cours.
*   **Interaction et Collaboration :** Forums de discussion dédiés à chaque cours. Messagerie interne avec les enseignants et autres étudiants. Possibilité de soumettre des travaux. Accès à des classes virtuelles ou visioconférences.
*   **Évaluations :** Participation à des quiz et examens en ligne. Soumission de devoirs. Participation aux sondages. Consultation des notes et retours des enseignants.
*   **Notifications :** Alertes pour les nouvelles annonces, devoirs, ou messages.

---

## Technologies Utilisées

*   **Framework Web :** Django (Python)
*   **Base de Données :** MySQL (configurable, SQLite par défaut pour le développement)
*   **Front-end :** Django Templates (HTML, CSS, JavaScript)
    *   **Styling :** Bootstrap
    *   **Interactivité :** Vanilla JavaScript (avec appels AJAX pour les opérations CRUD dynamiques)
*   **Environnement :** Python 3.x

---

## Installation et Configuration

Suivez ces étapes pour configurer et lancer le projet en local.

### Prérequis

*   Python 3.x
*   Un environnement virtuel (fortement recommandé)

### Étapes de Configuration

1.  **Cloner le dépôt GitHub :**
    ```bash
    git clone https://github.com/votre-utilisateur/E-ISTC-Platform.git
    cd E-ISTC-Platform
    ```

2.  **Créer et activer un environnement virtuel :**
    *   **Pour Windows :**
        ```bash
        python -m venv venv_windows
        venv_windows\Scripts\activate
        ```
    *   **Pour macOS/Linux :**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Installer les dépendances :**
    Le projet utilise Django et `python-dotenv`.
    ```bash
    pip install Django python-dotenv
    ```

4.  **Configurer les variables d'environnement :**
    Créez un fichier `.env` à la racine du dossier `e_istc/` (c'est-à-dire `e_istc/.env`) et ajoutez-y les variables suivantes :
    ```
    DJANGO_SECRET_KEY='votre_clé_secrète_django_ici'
    DEBUG=True
    EMAIL_HOST_USER='votre_email@gmail.com'
    EMAIL_HOST_PASSWORD='votre_mot_de_passe_app_gmail' # Utilisez un mot de passe d'application pour Gmail
    ```
    *Remplacez les valeurs par vos propres informations. Pour `DJANGO_SECRET_KEY`, vous pouvez générer une chaîne aléatoire en ligne ou via Django.*

5.  **Appliquer les migrations de la base de données :**
    ```bash
    python e_istc/manage.py migrate
    ```

6.  **Créer un superutilisateur (administrateur) :**
    ```bash
    python e_istc/manage.py createsuperuser
    ```
    Suivez les invites pour créer votre compte administrateur.

---

## Lancer l'Application

Pour démarrer le serveur de développement Django :

```bash
python e_istc/manage.py runserver
```

L'application sera accessible à l'adresse : `http://127.0.0.1:8000`

---

## Exécuter les Tests

Le projet inclut une suite de tests pour chaque application. Pour exécuter tous les tests :

```bash
python e_istc/manage.py test
```

---

## Commandes de Gestion Personnalisées

Le projet dispose de commandes de gestion Django personnalisées pour des tâches de maintenance et de développement :

*   **`maintenance` :** Applique les migrations de la base de données et collecte les fichiers statiques.
    ```bash
    python e_istc/manage.py maintenance
    ```

*   **`backup` :** Crée une sauvegarde JSON de la base de données dans le répertoire `backups/`.
    ```bash
    python e_istc/manage.py backup
    ```
    *Exemple de fichier généré : `backups/backup_20250802_143000.json`*

*   **`restore <path_to_backup_file>` :** Restaure la base de données à partir d'un fichier de sauvegarde JSON spécifié.
    ```bash
    python e_istc/manage.py restore backups/backup_20250802_143000.json
    ```

*   **`seed_data` :** Remplit la base de données avec des données réalistes pour le développement et les tests. **Attention :** Cette commande supprime toutes les données existantes avant de les recréer.
    ```bash
    python e_istc/manage.py seed_data
    ```

---

## Conventions de Développement

*   **Conception Modulaire :** Le projet est organisé en applications Django distinctes, favorisant la séparation des préoccupations.
*   **Interface Utilisateur Dynamique :** Utilisation intensive de JavaScript et AJAX pour des opérations CRUD fluides sans rechargement de page, notamment dans les interfaces d'administration et de gestion des cours.
*   **Décorateurs de Permissions :** Des décorateurs personnalisés (`@admin_required`, `@course_owner_or_admin_required`, `@role_required`) sont utilisés pour appliquer des contrôles d'accès robustes aux vues et API.
*   **Notifications Asynchrones :** Les actions utilisateur sont confirmées par des notifications "toast" non bloquantes.
*   **Signaux Django :** Les signaux (`post_save`) sont employés pour déclencher automatiquement des notifications lors d'événements clés (nouvelles annonces, messages).
*   **Authentification Personnalisée :** Un backend d'authentification permet la connexion via email, nom d'utilisateur ou matricule étudiant.
*   **Emails Automatisés :** Envoi automatique d'emails de bienvenue avec un lien de définition de mot de passe lors de la création d'un utilisateur.

---

## Licence

Ce projet est sous licence [MIT](LICENSE) (ou toute autre licence que vous choisissez).

---
