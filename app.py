import sqlite3  # Built-in module for interacting with SQLite databases

from flask import Flask, redirect, render_template, request

app = Flask(__name__)  # Initialize Flask app

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('inventory.db')  # Connects to (or creates) inventory.db
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

# Home route – displays all inventory items
@app.route('/')
def index():
    conn = get_db_connection()  # Open DB connection
    items = conn.execute('SELECT * FROM items').fetchall()  # Fetch all rows
    conn.close()  # Close DB connection
    return render_template('index.html', items=items)  # Render the inventory list

# Route to add a new item – handles form display and submission
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':  # If form is submitted
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        category = request.form['category']

        conn = get_db_connection()
        conn.execute('INSERT INTO items (name, quantity, price, category) VALUES (?, ?, ?, ?)', (name, quantity, price, category))  # Insert new item into DB
        conn.commit()
        conn.close()
        return redirect('/')  # Redirect to homepage after adding
    return render_template('add.html')  # Show the add item form

# Route to delete an item by its ID
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))  # Delete item by ID
    conn.commit()
    conn.close()
    return redirect('/')  # Redirect to homepage after deletion

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for easier testing
