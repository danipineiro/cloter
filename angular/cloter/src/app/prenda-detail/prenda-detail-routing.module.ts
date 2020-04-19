import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PrendaDetailPage } from './prenda-detail.page';

const routes: Routes = [
  {
    path: '',
    component: PrendaDetailPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PrendaDetailPageRoutingModule {}
