import { Component, OnInit } from '@angular/core';
import { Mesa } from '../../../modelos/mesa.model';
import { MesaService } from '../../../servicios/mesa.service';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';

@Component({
  selector: 'ngx-listar-mesas',
  templateUrl: './listar-mesas.component.html',
  styleUrls: ['./listar-mesas.component.scss']
})
export class ListarMesasComponent implements OnInit {
  mesas : Mesa[];
  nombresColumnas: string[] = ['numero','cantidad inscritos'];

  constructor(private miServicioMesa: MesaService, private router: Router) { }

  ngOnInit(): void {
    this.listar();
  }
  listar():void{
    this.miServicioMesa.listar().
      subscribe(data => {
        this.mesas=data;
      });
  }
  agregar():void{
    this.router.navigate(["pages/mesas/crear-mesas"])
    console.log("agregando nuevo")
  }
  editar(id:string):void{
    this.router.navigate(["pages/mesas/actualizar/"+id])
    console.log("editando a "+id)
  }
  eliminar(id:string):void{
    Swal.fire({
      title: 'Eliminar Mesa',
      text: "Está seguro que quiere eliminar la mesa?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, eliminar'
    }).then((result) => {
      if (result.isConfirmed) {
        this.miServicioMesa.eliminar(id).
          subscribe(data => {
            Swal.fire(
              'Eliminado!',
              'La mesa ha sido eliminada correctamente',
              'success'
            )
            this.ngOnInit();
          });
      }
    })
  }

}
