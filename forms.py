from flask import Flask #? Importamos la clase Flask del módulo flask
#?Importamos la clase FlaskForm del módulo flask_wtf
from flask_wtf import FlaskForm
#? Importamos los distintos campos que usaremos en el formulario del módulo wtforms
from wtforms import (
    StringField, # Campo para ingresar texto
    PasswordField, # Campo para ingresar contraseñas
    BooleanField) # Campo para ingresar valores booleanos (True o False)
#? Importamos los distintos validadores que usaremos en los campos del formulario del módulo wtforms
from wtforms.validators import (
    DataRequired, # Validador para asegurarse de que se proporciona algún dato
    InputRequired, # Validador para asegurarse de que se proporciona un dato de entrada
    Email, # Validador para asegurarse de que se proporciona un correo electrónico válido
    Length ## Validador para asegurarse de que la longitud de un campo está dentro de un rango específico
    )
#?-----------------------Login Form ---------------------------------------------
#*  Definimos la clase LoginForm que hereda de FlaskForm para usar en html con jinja2
class Loginform(FlaskForm): 
    # Definimos los campos del formulario junto con sus validadores
    #this news changes help us for customizing the error messsages from our templates so we can have messages in spanish
    username = StringField('username', validators=[InputRequired(message= 'Este campo requiere completarse'),
    Length(min= 4 ,max =16, message= 'El Nombre de Usuario debe tener entre %(min)d y %(max)d Caracteres')])
    
    password= PasswordField('password', validators=[InputRequired(message= 'Este campo requiere completarse'),
    Length(min= 8 ,max =16 , message= 'la contraseña debe etener entre  %(min)d y %(max)d Caracteres')])
    
    remember = BooleanField('Recuerda me')
    
#? ----------------------Register Form ----------------------------------------------
class CreateUserForm(FlaskForm): 
    # Definimos los campos del formulario junto con sus validadores
    email = StringField('Escribe el Correo Electronico', validators=[InputRequired(message= 'Este campo requiere completarse'), Email(message="Este no es un correo electronico valido"), 
    Length(max =60 , message= 'El Nombre de Usuario debe tener  %(max)d Caracteres')])
    username = StringField('Escribe el Nombre de Usuario', validators=[InputRequired(message= 'Este campo requiere completarse'),
    Length(min= 4 ,max =16 , message= 'El Nombre de Usuario debe tener entre %(min)d y %(max)d Caracteres')]) # ahora puede cambiar el nombre de los label de l formulario desde aqui
    password= PasswordField('Agrega una Contraseña', validators=[InputRequired(message= 'Este campo requiere completarse'), 
    Length(min= 8 ,max =16 , message= 'la contraseña debe etener entre  %(min)d y %(max)d Caracteres')])
    