import sqlite3

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('index.html', items=items, search=False)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        category = request.form['category']

        if not name or not quantity or not price or not category:
            return "All fields are required!", 400
        if int(quantity) < 0:
            return "Quantity cannot be negative!", 400
        if float(price) < 0:
            return "Price cannot be negative!", 400

        conn = get_db_connection()
        conn.execute('INSERT INTO items (name, quantity, price, category) VALUES (?, ?, ?, ?)', (name, quantity, price, category))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/search')
def search():
    query = request.args.get('query')
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items WHERE name LIKE ?', ('%' + query + '%',)).fetchall()
    conn.close()
    return render_template('index.html', items=items, search=True)

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        category = request.form['category']

        if not name or not quantity or not price or not category:
            return "All fields are required!", 400
        if int(quantity) < 0:
            return "Quantity cannot be negative!", 400
        if float(price) < 0:
            return "Price cannot be negative!", 400

        conn.execute('UPDATE items SET name = ?, quantity = ?, price = ?, category = ? WHERE id = ?', (name, quantity, price, category, id))
        conn.commit()
        conn.close()
        return redirect('/')

    conn.close()
    return render_template('edit.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
