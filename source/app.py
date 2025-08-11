from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message

# modulo para entorno local
# from config import USUARIO_GMAIL, PASSWORD_GMAIL, SECRET_KEY

# modulo para entorno de producción en Render
from source.config import USUARIO_GMAIL, PASSWORD_GMAIL, SECRET_KEY

# modulo para entorno local
from routes.sitio import sitio

# modulo para entorono de producción en Render
from source.routes.sitio import sitio







app= Flask(__name__)

app.secret_key = SECRET_KEY
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USERNAME']= f'{USUARIO_GMAIL}'
app.config['MAIL_PASSWORD']= f'{PASSWORD_GMAIL}'
app.config['MAIL_DEFAULT_SENDER']= f'{USUARIO_GMAIL}'
mail= Mail(app)

# app.config['SECRET_KEY']= f'{SECRET_KEY}'

# app.config['JWT_SECRET_KEY']= f'{SECRET_JWT}'
# JWT= JWTManager(app)

app.register_blueprint(sitio)




                                                              
if __name__ == '__main__':
    app.run(debug=True)
