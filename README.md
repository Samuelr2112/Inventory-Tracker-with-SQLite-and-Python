# 📦 Inventory Tracker with SQLite and Python

This is a lightweight full-stack web application I built using Flask (Python) for the backend and plain HTML/CSS for the frontend.  
It’s a simple, clean app to manage inventory items — including name, quantity, price, and category — with persistent data storage using SQLite.

The project includes a working CRUD interface (Create, Read, Update, Delete), a search feature to find items by name, and input validation to prevent bad data entries.

---

## 🔍 What It Does
- ✅ Add, edit, delete, and list inventory items (name, quantity, price, category)
- 🔎 Search inventory items by name
- 🛡️ Input validation to ensure proper data (no negative values, all fields required)
- 📦 Persistent database storage using SQLite
- 💻 Frontend built with plain HTML and basic styling

---

## 🧰 Tech Stack
- Python 3.12+
- Flask (Micro web framework)
- SQLite (Lightweight database)
- HTML5 + CSS (Basic UI)

---
```
## 📁 Project Structure
Inventory Tracker with SQLite and Python/
├── app.py
├── inventory.db
├── /templates
│    ├── index.html
│    ├── add.html
│    └── edit.html
└── (optional /static for future CSS or images)
```
---
## 🚀 How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/Samuelr2112/Inventory-Tracker-with-SQLite-and-Python.git
cd Inventory-Tracker-with-SQLite-and-Python
```
2. Install Flask
Make sure Flask is installed:
```
bash
Copy
Edit
pip install flask
(You don't need to install SQLite — it comes built-in with Python.)
```
3. Start the App
Run the Flask app:
```
bash
Copy
Edit
python app.py
The server will start at:

cpp
Copy
Edit
http://127.0.0.1:5000
```
4. Use the App
Open your browser and go to http://127.0.0.1:5000

Add, edit, delete, and search inventory items

All changes are saved in the inventory.db SQLite database
```
👨‍💻 Why I Built This
I built this project to practice building a full CRUD web app with a lightweight backend.
I wanted something simple but fully functional, using only Flask, SQLite, and basic HTML — no heavy frameworks.
It’s easy to set up, runs locally, and doesn't require any complex installations.

Feel free to explore it and test the features!
