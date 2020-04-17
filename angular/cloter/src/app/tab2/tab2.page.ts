import {Component, OnInit} from '@angular/core';
import {PrendaService} from "../prenda/prenda.service";

@Component({
    selector: 'app-tab2',
    templateUrl: 'tab2.page.html',
    styleUrls: ['tab2.page.scss']
})
export class Tab2Page implements OnInit {

    public loading = true;
    public prenda_1: any;
    public prenda_2: any;

    constructor(
        private prendaService: PrendaService
    ) {
    }

    ngOnInit(): void {
        this.getParejaprendasRandom();
    }

    private getParejaprendasRandom() {
        this.prendaService.getParejaPrendasRandom().subscribe(
            (response: any) => {
                this.prenda_1 = response[1];
                this.prenda_2 = response[0];
                this.loading = false;
            });
    }

    public enviarMatch(){
        this.getParejaprendasRandom();
    }

}
