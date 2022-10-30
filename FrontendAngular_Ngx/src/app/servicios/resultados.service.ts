import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Resultados } from '../modelos/resultados.model';
import { Usuario } from '../modelos/usuario.model';
@Injectable({
providedIn: 'root'
})
export class ResultadosService {
constructor(private http: HttpClient) { }
listar(): Observable<Resultados[]> {
  return this.http.get<Resultados[]>(`${environment.url_gateway}/resultados`);
}
eliminar(id:string){
  return this.http.delete<Resultados>(`${environment.url_gateway}/resultados/${id}`,);
}
getresultado(id:string): Observable<Resultados>{
  return this.http.get<Resultados>(`${environment.url_gateway}/resultados/${id}`);
}
crear(elResultado: Resultados){
 return this.http.post(`${environment.url_gateway}/resultados`,elResultado);
}
editar(id:string,elResultado: Resultados){
  return this.http.put(`${environment.url_gateway}/resultados/${id}/candidato/${id}/mesa/${id}`,elResultado);
}
}
