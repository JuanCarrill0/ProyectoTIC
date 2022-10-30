from flask import request
from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        numero = infoMesa['numero']
        cant_inscritos = infoMesa['cant_inscritos']
        mesas = self.repositorioMesa.findAll()

        for mesa in mesas:
            if mesa['numero'] == numero:
                return 'Ha ocurrido el siguiente error : El numero de la mesa ya existe'

        if numero == "" or cant_inscritos == "":
            return 'Ha ocurrido el siguiente error : Alguno de los parametros esta vacio'
        else:
            nuevaMesa = Mesa(infoMesa)
            return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        numero = infoMesa['numero']
        cant_inscritos = infoMesa['cant_inscritos']
        laMesa = Mesa(self.repositorioMesa.findById(id))
        mesas = self.repositorioMesa.findAll()

        for mesa in mesas:
            if mesa['numero'] == numero and numero != laMesa.numero:
                return 'Ha ocurrido el siguiente error : El numero de la mesa ya existe y no corresponde al id solicitado'

        if numero == "" or cant_inscritos == "":
            return 'Ha ocurrido el siguiente error : Alguno de los parametros esta vacio'
        else:
            mesaActual = Mesa(self.repositorioMesa.findById(id))
            mesaActual.numero = infoMesa["numero"]
            mesaActual.cant_inscritos = infoMesa["cant_inscritos"]
            return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)


