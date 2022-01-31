from flask import Flask, render_template, request, redirect
from flask_app.modelos.usuario import Usuarios
from flask_app import app

@app.route('/')
def inicio():
    return redirect('/usuarios')

@app.route("/usuarios", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/listaUsuarios', methods=['GET'])
def listaUsuario():
    usuarios = Usuarios.seleccionar()
    print("Ruta /listaUsuarios",usuarios)
    return render_template("lista.html", all_usuarios = usuarios)

@app.route("/nuevoUsuario", methods=["POST"])
def agregarUsuario():
    datosUsuarios ={
        "first_name" : request.form["nombre"],
        "last_name" : request.form["apellido"],
        "email" : request.form["email"] 
    }
    Usuarios.guardar( datosUsuarios )
    return redirect('/listaUsuarios')

@app.route("/editarUsuario/<int:id>", methods=["GET"])
def editarUsuario( id ):
    datosUsuarios = {
        "id" : id
    }
    usuario = Usuarios.seleccionarUno( datosUsuarios )
    #print("valores de la lista", usuario)
    return render_template("editusers.html", usuario=usuario)

"""OJO: NO TE OLVIDES DE PONERLE EL <id a la ruta tambien>
        <form action="/actualizar/{{usuario.id}}" method="POST">

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar( id ):
    #print("valor del id",request.form['id'])
    data = {
        "id" : request.form["id"],
        "first_name" : request.form["nombre"],
        "last_name" : request.form["apellido"],
        "email" : request.form["email"]         
    }
    usuario = Usuarios.update( data )
    #print("respuesta request",request.form)
    return redirect('/listaUsuarios')
"""

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    data ={
        "id" : id,
        "first_name" : request.form["nombre"],
        "last_name" : request.form["apellido"],
        "email" : request.form["email"]         
    }
    usuario = Usuarios.update( data )
    return redirect('/listaUsuarios')


@app.route("/mostratUsuario/<int:id>", methods=["GET"])
def mostratUsuario( id ):
    datosUsuarios = {
        "id" : id
    }
    usuario = Usuarios.seleccionarUno ( datosUsuarios )
    #print("Aqui info mostrarUsuario del server.py", usuario.__dict__)
    return render_template("viewUser.html", usuario = usuario)

@app.route('/eliminarUsuario/<int:id>', methods=['GET'])
def eliminarUsuario( id ):
    datosUsuarios = {
        "id" : id
    }
    usuario = Usuarios.eliminar ( datosUsuarios )
    print("que tiene usuario", usuario)
    return redirect('/listaUsuarios')