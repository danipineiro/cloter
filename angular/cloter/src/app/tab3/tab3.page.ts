import {Component, OnInit} from '@angular/core';
import {PrendaService} from "../prenda/prenda.service";

@Component({
    selector: 'app-tab3',
    templateUrl: 'tab3.page.html',
    styleUrls: ['tab3.page.scss']
})
export class Tab3Page implements OnInit {

    public listaPrendas = [];

    constructor(
        private prendaService: PrendaService
    ) {
    }

    ngOnInit(): void {
        this.prendaService.getPrendas().subscribe(
            (response: any) => {
                this.listaPrendas = response.results;
            });
    }

}
