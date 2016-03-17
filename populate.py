import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurantes.settings')

import django
django.setup()

from app_restaurantes.models import Restaurante, Plato


def populateRestaurantes():
    
    addRestaurante(nombre="Soy un Restaurante!", direccion="direccion1", email="algo1@algo.com", telefono="958765665")
    addRestaurante(nombre="Restaurante 2", direccion="direccion2", email="algo2@algo.com", telefono="958165665")
    addRestaurante(nombre="Restaurante 3", direccion="direccion3", email="algo3@algo.com", telefono="958265665")
    addRestaurante(nombre="Restaurante 4", direccion="direccion4", email="algo4@algo.com", telefono="958365665")
    addRestaurante(nombre="Restaurante 5", direccion="direccion5", email="algo5@algo.com", telefono="958465665")
    addRestaurante(nombre="Restaurante 6", direccion="direccion6", email="algo6@algo.com", telefono="958565665")
    addRestaurante(nombre="Restaurante 7", direccion="direccion7", email="algo7@algo.com", telefono="958665665")
    

    # Print out what we have added to the user.
    for r in Restaurante.objects.all():
        print "- {0} ".format(str(r))

def populatePlatos():
    p = Plato(nombre="Plato!", descripcion="Soy un plato!!", comentarios=["es bueno!","yo creo que no..","yo soy un comentario!"])
    p.save()
    p = Plato(nombre="Otro plato", descripcion="otro plato..", comentarios=["es bueno!","yo creo que no..","yo soy un comentario!"])
    p.save()

    # Print out what we have added to the user.
    for r in Plato.objects:
        print "- {0} ".format(str(r))

def addRestaurante(nombre, direccion, email, telefono):
    r = Restaurante(nombre=nombre)
    r.direccion = direccion
    r.email = email
    r.telefono = telefono
    
    r.save()
    return r


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    #populateRestaurantes()
    populatePlatos()

