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

## 📁 Project Structure
Inventory Tracker with SQLite and Python/
├── app.py
├── inventory.db
├── /templates
│    ├── index.html
│    ├── add.html
│    └── edit.html
└── (optional /static for future CSS or images)


yaml
Copy
Edit

---

## 🚀 How to Run

### 1. Install Dependencies
You only need Flask. Install it with pip:

``bash
pip install flask
SQLite comes pre-installed with Python.

2. Start the Flask App
In your project directory:

bash
Copy
Edit
python app.py
It will run on:

bash
Copy
Edit
http://127.0.0.1:5000
Open it in your browser.

3. Use the Web Interface
View all inventory items

Add a new item

Edit an existing item

Delete an item (with confirmation)

Search for items by name

👨‍💻 Why I Built This
I built this project to practice building a full CRUD web app with a lightweight backend.
I wanted something simple but fully functional, using only Flask, SQLite, and basic HTML — no heavy frameworks.
It’s easy to set up, runs locally, and doesn't require any complex installations.

Feel free to explore it and test the features!

🛠️ Next Possible Improvements
Add user authentication (simple login system)

Improve UI with Bootstrap or TailwindCSS

Add item sorting and filtering

Deploy it online using Render or Railway

✨ About
No special setup required — clone, install Flask, and run!

