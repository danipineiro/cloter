import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class PrendaService {

  API_URL = 'http://localhost/api/';

  constructor(
    private http: HttpClient,
  ) {
  }

  public getPrendas() {
    return this.http.get(`${this.API_URL}prendas/`)
  }

  public getParejaPrendasRandom() {
    return this.http.get(`${this.API_URL}prendas/pareja_random`)
  }

  getPrendaDetail(id: number) {
    return this.http.get(`${this.API_URL}prendas/${id}`)
  }
}
