import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarMesasComponent } from './listar-mesas.component';

describe('ListarMesasComponent', () => {
  let component: ListarMesasComponent;
  let fixture: ComponentFixture<ListarMesasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListarMesasComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarMesasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
