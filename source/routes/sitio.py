from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for
from flask_mail import Mail, Message


sitio= Blueprint('sitio', __name__)

@sitio.route('/')
def inicio():
    return render_template('sitio/index.html') 

@sitio.route('/service')
def servicios():
    return render_template('sitio/service.html')
    
@sitio.route('/profile')
def perfil_admin():
    return render_template('sitio/profile.html')


@sitio.route('/contacto', methods=['GET', 'POST'])
def contacto():
    mail = Mail(current_app)
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')

        asunto = f'Nuevo mensaje de {nombre}'
        cuerpo = f'Nombre: {nombre}\nEmail: {email}\nMensaje:\n{mensaje}'

        msg = Message(subject=asunto,
                      sender=current_app.config['MAIL_DEFAULT_SENDER'],
                      recipients=[current_app.config['MAIL_USERNAME']],
                      body=cuerpo)
        try:
            mail.send(msg)
            flash('El Mensaje fue enviado correctamente! Pronto me pondré en Contacto con Vos. ¡Muchas Gracias!', 'success')
        except Exception as e:
            flash(f'Error al enviar mensaje: {str(e)}', 'danger')

        # Detectar la página que envió el formulario y redirigir ahí:
        referrer = request.referrer  # URL completa de la página de origen
        if referrer:
            # Extraer solo el path, por ejemplo '/service' o '/'
            from urllib.parse import urlparse
            path = urlparse(referrer).path
            return redirect(path)
        
        # fallback
        return redirect(url_for('sitio.inicio'))

    return render_template('sitio/index.html')








