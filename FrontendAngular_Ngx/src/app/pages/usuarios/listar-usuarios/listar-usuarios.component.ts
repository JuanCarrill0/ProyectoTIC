import { Component, OnInit } from '@angular/core';
import { Usuario } from '../../../modelos/usuario.model';
import { UsuarioService } from '../../../servicios/usuario.service';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';

@Component({
  selector: 'ngx-listar-usuarios',
  templateUrl: './listar-usuarios.component.html',
  styleUrls: ['./listar-usuarios.component.scss']
})
export class ListarUsuariosComponent implements OnInit {
  usuarios : Usuario[];
  nombresColumnas: string[] = ['seudonimo','correo','opciones'];
  constructor(private miServicioUsuario: UsuarioService, private router: Router) { }

  ngOnInit(): void {
    this.listar();
  }
  listar():void{
    this.miServicioUsuario.listar().
      subscribe(data => {
        this.usuarios=data;
      });
  }
  agregar():void{
    this.router.navigate(["pages/usuarios/registrarse"])
  }
  editar(id:string):void{
    this.router.navigate(["pages/usuarios/actualizar/"+id])
  }
  eliminar(id:string):void{
    Swal.fire({
      title: 'Eliminar Usuario',
      text: "Está seguro que quiere eliminar el Usuario?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, eliminar'
    }).then((result) => {
      if (result.isConfirmed) {
        this.miServicioUsuario.eliminar(id).
          subscribe(data => {
            Swal.fire(
              'Eliminado!',
              'El Usuario ha sido eliminada correctamente',
              'success'
            )
            this.ngOnInit();
          });
      }
    })
  }
}