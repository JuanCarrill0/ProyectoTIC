from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        cedula = infoCandidato['cedula']
        num_resolucion = infoCandidato['num_resolucion']
        nombre = infoCandidato['nombre']
        apellido = infoCandidato['apellido']
        if cedula == "" or num_resolucion == "" or nombre == "" or apellido == "":
            return 'Ha ocurrido el siguiente error : Alguno de los parametros esta vacio'
        else:
            nuevoCandidato = Candidato(infoCandidato)
            return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        cedula = infoCandidato['cedula']
        num_resolucion = infoCandidato['num_resolucion']
        nombre = infoCandidato['nombre']
        apellido = infoCandidato['apellido']
        if cedula == "" or num_resolucion == "" or nombre == "" or apellido == "":
            return 'Ha ocurrido el siguiente error : Alguno de los parametros esta vacio'
        else:
            candidatoActual = Candidato(self.repositorioCandidato.findById(id))
            candidatoActual.cedula = infoCandidato["cedula"]
            candidatoActual.num_resolucion = infoCandidato["num_resolucion"]
            candidatoActual.nombre = infoCandidato["nombre"]
            candidatoActual.apellido = infoCandidato["apellido"]
            return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        return self.repositorioCandidato.delete(id)

    """
    Relacion 1..n partido y candidato
    """
    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        if hasattr(candidatoActual, 'partido'):
            return 'Ha ocurrido el siguiente error : El candidato ya se encuentra inscrito en un partido'
        else:
            partidoActual = Partido(self.repositorioPartido.findById(id_partido))
            candidatoActual.partido = partidoActual
            return self.repositorioCandidato.save(candidatoActual)