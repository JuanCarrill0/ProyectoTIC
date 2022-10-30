import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearMesasComponent } from './crear-mesas.component';

describe('CrearMesasComponent', () => {
  let component: CrearMesasComponent;
  let fixture: ComponentFixture<CrearMesasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CrearMesasComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CrearMesasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
