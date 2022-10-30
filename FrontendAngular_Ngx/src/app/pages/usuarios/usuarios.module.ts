import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UsuariosRoutingModule } from './usuarios-routing.module';
import { ListarUsuariosComponent } from './listar-usuarios/listar-usuarios.component';
import { NbCardModule } from '@nebular/theme';
import { RegistrarseComponent } from './registrarse/registrarse.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    ListarUsuariosComponent,
    RegistrarseComponent
  ],
  imports: [
    CommonModule,
    UsuariosRoutingModule,
    NbCardModule,
    FormsModule
  ]
})
export class UsuariosModule { }
