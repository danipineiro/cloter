import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PrendaDetailPageRoutingModule } from './prenda-detail-routing.module';

import { PrendaDetailPage } from './prenda-detail.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PrendaDetailPageRoutingModule
  ],
  declarations: [PrendaDetailPage]
})
export class PrendaDetailPageModule {}
