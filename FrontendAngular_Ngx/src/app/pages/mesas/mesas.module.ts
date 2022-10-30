import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MesasRoutingModule } from './mesas-routing.module';
import { ListarMesasComponent } from './listar-mesas/listar-mesas.component';
import { NbCardModule } from '@nebular/theme';
import { CrearMesasComponent } from './crear-mesas/crear-mesas.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    ListarMesasComponent,
    CrearMesasComponent
  ],
  imports: [
    CommonModule,
    MesasRoutingModule,
    NbCardModule,
    FormsModule
  ]
})
export class MesasModule { }
