import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PaginaPrincipalRoutingModule } from './pagina-principal-routing.module';
import { PrincipalComponent } from './principal/principal.component';


@NgModule({
  declarations: [
    PrincipalComponent
  ],
  imports: [
    CommonModule,
    PaginaPrincipalRoutingModule
  ]
})
export class PaginaPrincipalModule { }
