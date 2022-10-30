import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListarUsuariosComponent } from './listar-usuarios/listar-usuarios.component';
import { RegistrarseComponent } from './registrarse/registrarse.component';

const routes: Routes = [
  {
    path: 'listar-usuarios',
    component: ListarUsuariosComponent
    },
    {
      path: 'registrarse',
      component: RegistrarseComponent
      },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UsuariosRoutingModule { }
