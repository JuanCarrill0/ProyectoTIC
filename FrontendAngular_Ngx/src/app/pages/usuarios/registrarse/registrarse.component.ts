import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import Swal from 'sweetalert2';
import { Usuario } from '../../../modelos/usuario.model';
import { UsuarioService } from '../../../servicios/usuario.service';

@Component({
  selector: 'ngx-registrarse',
  templateUrl: './registrarse.component.html',
  styleUrls: ['./registrarse.component.scss']
})
export class RegistrarseComponent implements OnInit {
  modoCreacion: boolean = true;
  id_usuario: string = "";
  intentoEnvio: boolean = false;
  elUsuario: Usuario = {
    seudonimo: "",
    correo: "",
    contrasena: ""
  }
  constructor(private miServicioUsuario: UsuarioService,
    private rutaActiva: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    if (this.rutaActiva.snapshot.params.id_estudiante) {
      this.modoCreacion = false;
      this.id_usuario = this.rutaActiva.snapshot.params.id_estudiante;
      this.getUsuario(this.id_usuario)
    } else {
      this.modoCreacion = true;
    }
  }
  getUsuario(id: string) {
    this.miServicioUsuario.getUsuario(id).
      subscribe(data => {
        this.elUsuario = data;
      });
  }
  agregar(): void {
    if (this.validarDatosCompletos()) {
      this.intentoEnvio = true;
      this.miServicioUsuario.crear(this.elUsuario).
        subscribe(data => {
          Swal.fire(
            'Creado',
            'El usuario ha sido creado correctamente',
            'success'
          )
          this.router.navigate(["pages/usuarios/listar-usuarios"]);
        });
    }

  }
  editar(): void {
    this.intentoEnvio = true;
    if (this.validarDatosCompletos()) {
      this.miServicioUsuario.editar(this.elUsuario._id, this.elUsuario).
        subscribe(data => {
          Swal.fire(
            'Actualizado',
            'El usuario ha sido actualizado correctamente',
            'success'
          )
          this.router.navigate(["pages/usuarios/listar-usuarios"]);
        });
    }

  }
  validarDatosCompletos():boolean{
    this.intentoEnvio=true;
    if(this.elUsuario.seudonimo=="" || 
       this.elUsuario.correo=="" || 
       this.elUsuario.contrasena==""){
        
      return false;
    }else{
      return true;
    }
  }
}
