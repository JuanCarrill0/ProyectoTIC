from flask import request, Response, jsonify
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioReporte import RepositorioReporte
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidatos = RepositorioCandidato()
        self.repositorioMesas = RepositorioMesa()
        self.repositorioReportes = RepositorioReporte()

    def index(self):
        return self.repositorioResultado.findAll()

    """
        Asignacion mesa y candidato a resultado
    """

    def create(self,infoResultado,id_candidato,id_mesa):
        votos = infoResultado['cant_votos']
        elCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        inscritos = laMesa.cant_inscritos
        if votos == "" or votos == None:
            return 'Ha ocurrido el siguiente error : La cantidad de votos esta vacia'
        else:
            if inscritos >= votos:
                nuevoResultado = Resultado(infoResultado)
                nuevoResultado.candidato = elCandidato
                nuevoResultado.mesa = laMesa
                return self.repositorioResultado.save(nuevoResultado)
            else:
                return 'Ha ocurrido el siguiente error - La cantidad de inscritos es menor a la cantidad de votos'

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
        Modificación de resultado (mesa y candidato)
    """

    def update(self, id, infoResultado,id_candidato,id_mesa):
        elCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        votos = infoResultado['cant_votos']
        inscritos = laMesa.cant_inscritos
        if votos == "" or votos == None:
            return 'Ha ocurrido el siguiente error : La cantidad de votos esta vacia'
        else:
            if inscritos >= votos:
                elResultado = Resultado(self.repositorioResultado.findById(id))
                elResultado.cant_votos = infoResultado["cant_votos"]
                elResultado.candidato = elCandidato
                elResultado.mesa = laMesa
                return self.repositorioResultado.save(elResultado)
            else:
                return 'Ha ocurrido el siguiente error : La cantidad de inscritos es menor a la cantidad de votos'

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    def ListadoVotosEnMesas(self):
        return self.repositorioReportes.ListadoVotosEnMesas()

    def ListadoVotosCandidatos(self):
        return self.repositorioReportes.ListadoVotosCandidatos()

    def ListadoVotosCandidato(self, id_mesa):
        return self.repositorioReportes.ListadoVotosCandidato(id_mesa)
    
    def ListadoPartidosVotos(self, id_mesa=""):
        return self.repositorioReportes.ListadoPartidosVotos(id_mesa)

    def ListadoCongreso(self):
        return self.repositorioReportes.ListadoCongreso()