import {Component, OnInit} from '@angular/core';
import {PrendaService} from "../prenda/prenda.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-prenda-detail',
  templateUrl: './prenda-detail.page.html',
  styleUrls: ['./prenda-detail.page.scss'],
})
export class PrendaDetailPage implements OnInit {

  prendaId: any;
  prendaData: any;

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
      },
      (error: any) => {
        console.log(error);
      })
  }

}
