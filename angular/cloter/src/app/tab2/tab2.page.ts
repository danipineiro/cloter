import {Component, OnInit} from '@angular/core';
import {PrendaService} from "../prenda/prenda.service";

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page implements OnInit{

  public loading = true;
  public prenda_1: any;
  public prenda_2: any;

  constructor(
      private prendaService: PrendaService
  ) {}

  ngOnInit(): void {
        this.prendaService.getPrendas().subscribe(
            (response: any) => {
                this.prenda_1 = response.results[2];
                this.prenda_2 = response.results[3];
                this.loading = false;
            });
    }

}
