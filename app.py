from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, static_folder='static', template_folder='templates') # Create a Flask application instance
def init_db():
    conn = sqlite3.connect("formulario.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mensajes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono NUMBER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/") # Define a route for the root URL
def index():
    return render_template("index.html")

@app.route("/flex") # Define a route for the /flex URL
def flex():
    return render_template("flex.html")

@app.route("/grid")
def grid():
    return render_template("grid.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/procesar", methods=["POST"]) 
def procesar():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    print(f"Nombre: {nombre}, Teléfono: {telefono}")
    

    if nombre and telefono:
        conn = sqlite3.connect("formulario.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mensajes (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True) # Run the application in debug mode