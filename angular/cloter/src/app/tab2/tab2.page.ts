import {Component, OnInit} from '@angular/core';
import {PrendaService} from "../prenda/prenda.service";
import {MatchService} from "../match/match.service";

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
        private prendaService: PrendaService,
        private matchService: MatchService,
    ) {
    }

    ngOnInit(): void {
        this.getParejaPrendasRandom();
    }

    private getParejaPrendasRandom() {
        this.prendaService.getParejaPrendasRandom().subscribe(
            (response: any) => {
                this.prenda_1 = response[1];
                this.prenda_2 = response[0];
                this.loading = false;
            });
    }

    public enviarMatch(accion: number) {
        this.matchService.enviarVoto(this.prenda_1.id, this.prenda_2.id, accion).subscribe(
            (response: any) => {
                this.getParejaPrendasRandom();
            },
            (error: any) => {
                this.getParejaPrendasRandom();
            });
    }

}
