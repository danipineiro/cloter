import {Component, OnInit} from '@angular/core';
import {PrendaService} from "../prenda/prenda.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss']
})
export class Tab3Page implements OnInit {

  public listaPrendas = [];

  constructor(
    private prendaService: PrendaService,
    private router: Router
  ) {
  }

  ngOnInit(): void {
    this.prendaService.getPrendas().subscribe(
      (response: any) => {
        this.listaPrendas = response.results;
      });
  }

  public abrirPrendaDetail(id: number) {
    console.log(id);
    this.router.navigateByUrl('/tabs/tab3/prenda-detail');
  }

}
