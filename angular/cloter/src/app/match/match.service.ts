import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';


@Injectable({
    providedIn: 'root'
})
export class MatchService {

    API_URL = 'http://localhost/api/';

    constructor(
        private http: HttpClient,
    ) {
    }

    public enviarVoto(prenda_1Id: number, prenda_2Id: number, accion: number) {
        const data = {
            prenda_1: prenda_1Id,
            prenda_2: prenda_2Id,
            accion: accion
        };

        return this.http.post(`${this.API_URL}match/`, data)
    }
}
