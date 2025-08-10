from flask import Blueprint, render_template, request, flash 


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





