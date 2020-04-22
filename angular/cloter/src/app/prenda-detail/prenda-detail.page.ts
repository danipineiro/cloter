import {Component, OnInit} from '@angular/core';
import {PrendaService} from "../prenda/prenda.service";
import {ActivatedRoute} from "@angular/router";
import {materialize} from "rxjs/operators";

@Component({
  selector: 'app-prenda-detail',
  templateUrl: './prenda-detail.page.html',
  styleUrls: ['./prenda-detail.page.scss'],
})
export class PrendaDetailPage implements OnInit {

  prendaId: any;
  prendaData: any;
  prendaMatches: any;
  loading = true;

  constructor(
    private prendaService: PrendaService,
    private activatedRoute: ActivatedRoute
  ) {
  }

  ngOnInit() {
    this.prendaId = this.activatedRoute.snapshot.paramMap.get('id');

    this.prendaService.getPrendaDetail(this.prendaId).subscribe(
      (response: any) => {
        this.prendaData = response;
        this.prendaService.getPrendaMatches(this.prendaId).subscribe((matches: any) => {
          this.prendaMatches = this.cleanMatches(matches);
          this.loading = false;
        })
      },
      (error: any) => {
        console.log(error);
      })
  }

  private cleanMatches(matches: any[]) {
    for (let match of matches) {
      const p1 = match.prenda_1;
      const p2 = match.prenda_2;

      delete match['prenda_1'];
      delete match['prenda_2'];

      if (p1.id == this.prendaId) {
        match['prenda'] = p2
      } else {
        match['prenda'] = p1
      }
    }
    return matches;
  }

}
