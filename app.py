from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    mensaje_enviado = False

    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        mensaje = request.form["mensaje"]

        # Fecha y hora
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Guardar en archivo
        with open("mensajes.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Fecha: {fecha}\n")
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Correo: {correo}\n")
            archivo.write(f"Mensaje: {mensaje}\n")
            archivo.write("-" * 40 + "\n")

        mensaje_enviado = True

    return render_template("index.html", enviado=mensaje_enviado)

if __name__ == "__main__":
    app.run()

