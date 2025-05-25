# 🌍 API GIEC - Données Climatiques

Ce projet est une API REST développée avec **Django** et **Django REST Framework**, suivant une architecture **MVC**, pour gérer et exposer des données climatiques issues des rapports du **GIEC (Groupe d'experts intergouvernemental sur l'évolution du climat)**.

---

## 🚀 Fonctionnalités

- 📦 Création, consultation, modification et suppression des rapports climatiques
- 🔍 Interface admin personnalisée pour la gestion des données
- 📡 Endpoints RESTful avec pagination, recherche et filtres

---

## 🧱 Architecture (MVC)

- **Modèle (Model)** : Représente les entités comme `RapportClimatique`
- **Vue (View)** : Gère les endpoints API (via `viewsets`)
- **Contrôleur** : Intégré dans les vues grâce à Django REST Framework
- **Sérialiseur** : Convertit les objets Python en JSON

---

## 🛠️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-compte/api-giec.git
cd api-giec

2. Créer un environnement virtuel

python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate

3. Installer les dépendances

pip install -r requirements.txt

4. Appliquer les migrations

python manage.py makemigrations
python manage.py migrate

5. Créer un superutilisateur

python manage.py createsuperuser

6. Lancer le serveur

python manage.py runserver

🔗 Endpoints principaux
Méthode	URL	Description
GET	/api/rapports/	Liste tous les rapports
POST	/api/rapports/	Crée un nouveau rapport
GET	/api/rapports/<id>/	Détaille un rapport spécifique
PUT	/api/rapports/<id>/	Met à jour un rapport
DELETE	/api/rapports/<id>/	Supprime un rapport
🔐 Accès à l'interface d'administration

    Lien : http://127.0.0.1:8000/admin/

    Connectez-vous avec le superutilisateur créé

📁 Structure du projet

api_giec/
│
├── models.py          # Modèles (M de MVC)
├── serializers.py     # Sérialiseurs pour l'API
├── views.py           # Vues API (V de MVC)
├── admin.py           # Interface d'administration
├── urls.py            # Routing interne à l'app
│
projet_giec/
├── settings.py        # Configuration du projet
├── urls.py            # URLs principales de l’API

📜 Licence

Ce projet est distribué sous licence MIT. Voir le fichier LICENSE pour plus d'informations.
🤝 Contribuer

Les contributions sont les bienvenues !
Tu peux proposer des pull requests, signaler des bugs ou suggérer des améliorations.
📬 Contact

Développé par [Ton Nom ou Organisation]
📧 Contact : contact@example.com
