import { Component, OnInit } from '@angular/core';
import { Mesa } from '../../../modelos/mesa.model';
import { MesaService } from '../../../servicios/mesa.service';
import Swal from 'sweetalert2';
import { ActivatedRoute,Router } from '@angular/router';
import { NONE_TYPE } from '@angular/compiler';

@Component({
  selector: 'ngx-crear-mesas',
  templateUrl: './crear-mesas.component.html',
  styleUrls: ['./crear-mesas.component.scss']
})
export class CrearMesasComponent implements OnInit {
  modoCreacion: boolean = true;
  id_mesa: string = "";
  intentoEnvio: boolean = false;
  laMesa: Mesa = {
    numero: "",
    cant_inscritos: 0
  }
  constructor(private miServicioMesa: MesaService,
    private rutaActiva: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      if (this.rutaActiva.snapshot.params.id_mesa) {
        this.modoCreacion = false;
        this.id_mesa = this.rutaActiva.snapshot.params.id_mesa;
        this.getMesa(this.id_mesa)
      } else {
        this.modoCreacion = true;
      }
    }
    getMesa(id: string) {
      this.miServicioMesa.getMesa(id).
        subscribe(data => {
          this.laMesa = data;
        });
    }
    agregar(): void {
      if (this.validarDatosCompletos()) {
        this.intentoEnvio = true;
        this.miServicioMesa.crear(this.laMesa).
          subscribe(data => {
            Swal.fire(
              'Creado',
              'La mesa ha sido creada correctamente',
              'success'
            )
            this.router.navigate(["pages/mesas/listar-mesas"]);
          });
      }
  
    }
    editar(): void {
      this.intentoEnvio = true;
      if (this.validarDatosCompletos()) {
        this.miServicioMesa.editar(this.laMesa._id, this.laMesa).
          subscribe(data => {
            Swal.fire(
              'Actualizado',
              'La mesa ha sido actualizada correctamente',
              'success'
            )
            this.router.navigate(["pages/mesas/listar-mesas"]);
          });
      }
  
    }
    validarDatosCompletos():boolean{
      this.intentoEnvio=true;
      if(this.laMesa.numero=="" || 
         this.laMesa.cant_inscritos == 0 ){
          
        return false;
      }else{
        return true;
      }
    }
}
