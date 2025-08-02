# Gemini Context: E-ISTC Django E-Learning Platform

## Project Overview

This project is a monolithic e-learning platform named "E-ISTC," built with the Django web framework. It serves three main user roles: **Administrators**, **Teachers (Enseignants)**, and **Students (Étudiants)**. The platform facilitates online course management, content delivery, evaluations, and communication.

The architecture is based on a standard Django project structure, with functionality logically separated into different apps:

*   `users`: Manages user accounts, roles (Admin, Teacher, Student), authentication, and profiles.
*   `courses`: Handles the creation and management of courses, modules, and resources.
*   `evaluations`: Manages evaluations like quizzes, assignments (devoirs), and surveys (sondages).
*   `forums`: Provides discussion forums for each course.
*   `messaging`: Implements a private messaging system between users.
*   `notifications`: Sends notifications to users for various events.
*   `administration`: A custom administration interface for managing the platform's core data (users, courses, categories, etc.) with dynamic, AJAX-powered UI features.
*   `platform_settings`: Allows administrators to customize the look and feel of the platform.

The front-end is rendered using Django Templates, enhanced with Bootstrap for styling and vanilla JavaScript for dynamic interactions (AJAX calls for CRUD operations without page reloads).

## Building and Running

### Prerequisites

*   Python 3.x
*   A virtual environment (recommended)

### Setup

1.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv_windows
    venv_windows\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    *No `requirements.txt` was found.* Based on the `e_istc/e_istc/settings.py` file, the core dependency is Django. You will also need `python-dotenv`.
    ```bash
    pip install Django python-dotenv
    ```

3.  **Apply database migrations:**
    ```bash
    python e_istc/manage.py migrate
    ```

4.  **Create a superuser (administrator):**
    ```bash
    python e_istc/manage.py createsuperuser
    ```

### Running the Development Server

```bash
python e_istc/manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

### Running Tests

The project contains a suite of tests for each application. To run all tests:

```bash
python e_istc/manage.py test
```

## Key Commands

The project includes custom management commands for maintenance tasks.

*   **Run Maintenance (Migrate & Collect Static):**
    ```bash
    python e_istc/manage.py maintenance
    ```

*   **Create a Database Backup:**
    ```bash
    python e_istc/manage.py backup
    ```
    This command creates a JSON backup of the database in the `backups/` directory.

*   **Restore from a Backup:**
    ```bash
    python e_istc/manage.py restore <path_to_backup_file>
    ```
    **Example:**
    ```bash
    python e_istc/manage.py restore backups/backup_20250802_143000.json
    ```

## Development Conventions

*   **Modular Design:** The project is organized into multiple Django apps, each responsible for a specific domain of functionality. This promotes separation of concerns and maintainability.
*   **Dynamic UI:** The administration and teacher dashboards heavily utilize JavaScript and AJAX to provide a smooth, single-page-like experience for CRUD operations (Create, Read, Update, Delete) without requiring full page reloads.
*   **Custom Decorators:** Permissions are enforced using custom decorators like `@admin_required`, `@course_owner_or_admin_required`, and `@role_required` to protect views and API endpoints.
*   **Asynchronous Feedback:** User actions are confirmed with non-blocking "toast" notifications, providing immediate feedback for operations like creating a user or updating a course.
*   **Signaling for Notifications:** Django signals (`post_save`) are used in the `notifications` app to automatically create notifications when key events occur, such as the creation of a new announcement or a new private message.
*   **Custom Authentication:** A custom authentication backend (`EmailOrMatriculeBackend`) allows users to log in with their email or their unique student ID (matricule) in addition to their username.
*   **Automated Emails:** Upon user creation, a welcome email is automatically sent containing a link to set their password, improving the onboarding process.
