from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="lovers6511", 
        database="dsa_tracker"
    )

# Home page
@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM problems ORDER BY date_added DESC")
    problems = cursor.fetchall()
    
    conn.close()
    
    return render_template('index.html', problems=problems)

# Add problem
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        difficulty = request.form['difficulty']
        status = request.form['status']

        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO problems (name, difficulty, status) VALUES (%s, %s, %s)",
            (name, difficulty, status)
        )
        
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add.html')

# Delete problem
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM problems WHERE id = %s", (id,))
    
    conn.commit()
    conn.close()
    
    return redirect('/')

# Run app
if __name__ == '__main__':
    app.run(debug=True)