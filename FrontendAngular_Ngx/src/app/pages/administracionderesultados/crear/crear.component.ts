import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import Swal from 'sweetalert2';
import { Resultados } from '../../../modelos/resultados.model';
import { ResultadosService } from '../../../servicios/resultados.service';
@Component({
selector: 'ngx-crear',
templateUrl: './crear.component.html',
styleUrls: ['./crear.component.scss']
})
export class CrearComponent implements OnInit {

modoCreacion: boolean = true;
id_resultado: string = "";
intentoEnvio: boolean = false;
elResultado: Resultados = {
id_candidato: "",
mun_mesa:"",
cantidad_de_votos: ""
}
constructor(private miServicioResultados: ResultadosService,
private rutaActiva: ActivatedRoute,
private router: Router) { }
ngOnInit(): void {
if (this.rutaActiva.snapshot.params.id_resultado) {
this.modoCreacion = false;
this.id_resultado = this.rutaActiva.snapshot.params.id_resultado;
this.getResultado(this.id_resultado)
} else {
this.modoCreacion = true;
}
}
getResultado(id: string) {
this.miServicioResultados.getresultado(id).
subscribe(data => {
this.elResultado = data;
});
}
agregar(): void {
if (this.validarDatosCompletos()) {
this.intentoEnvio = true;
this.miServicioResultados.crear(this.elResultado).subscribe(data => {
Swal.fire(
'Creado',
'El Resultado ha sido creado correctamente',
'success'
)
this.router.navigate(["pages/resultados/listar"]);
});
}
}
editar(): void {
if (this.validarDatosCompletos()) {
this.miServicioResultados.editar(this.elResultado.id_candidato,
this.elResultado).subscribe(data => {
  Swal.fire(
    'Actualizado',
    'El resultado ha sido actualizado correctamente',
    'success'
  )
  this.router.navigate(["pages/resultads/listar"]);
});
}

}
validarDatosCompletos():boolean{
this.intentoEnvio=true;
if(this.elResultado.id_candidato=="" ||
this.elResultado.mun_mesa=="" ||
this.elResultado.cantidad_de_votos==""){

return false;
}else{
return true;
}
}
}
