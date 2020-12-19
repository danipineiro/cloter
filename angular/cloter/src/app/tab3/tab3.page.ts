import {Component, ViewChild, OnInit} from '@angular/core';
import {IonInfiniteScroll} from '@ionic/angular';
import {PrendaService} from "../prenda/prenda.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss']
})
export class Tab3Page implements OnInit {
  @ViewChild(IonInfiniteScroll, {static: false}) infiniteScroll: IonInfiniteScroll;

  public listaPrendas = [];
  private page = 1;
  next = false;

  constructor(
    private prendaService: PrendaService,
    private router: Router
  ) {
  }

  ngOnInit(): void {
    this.cargarPrendas();
  }

  public abrirPrendaDetail(id: number) {
    this.router.navigateByUrl(`/members/tab3/prenda-detail/${id}`);
  }

  loadData(event) {
    setTimeout(() => {
      this.cargarPrendas();
      event.target.complete();

    }, 1000);
  }

  private cargarPrendas() {
    this.prendaService.getPrendas(this.page).subscribe(
      (response: any) => {
        this.next = response.next != null;
        if (this.next) {
          this.infiniteScroll.disabled = false;
          this.page++;
        } else {
          this.infiniteScroll.disabled = true;
        }
          this.listaPrendas = [...this.listaPrendas, ...response.results];
        console.log(this.listaPrendas)
      });
  }
}
