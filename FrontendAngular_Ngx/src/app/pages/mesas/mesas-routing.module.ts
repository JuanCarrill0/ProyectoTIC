import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListarMesasComponent } from './listar-mesas/listar-mesas.component';
import { CrearMesasComponent } from './crear-mesas/crear-mesas.component';

const routes: Routes = [
  {
    path: 'listar-mesas',
    component: ListarMesasComponent
  },
  {
    path: 'crear-mesas',
    component: CrearMesasComponent
  },
  {
    path: 'actualizar/:id_mesa',
    component: CrearMesasComponent
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MesasRoutingModule { }
