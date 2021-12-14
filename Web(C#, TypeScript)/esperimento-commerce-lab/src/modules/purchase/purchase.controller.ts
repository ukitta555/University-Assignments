import { Controller } from '@nestjs/common';
import { ControllerBase } from 'src/core/controller-base';
import { PurchaseService } from './purchase.service';

@Controller('purchase')
export class PurchaseController extends ControllerBase{
  constructor(
    private readonly purchaseService: PurchaseService
  ) {super(purchaseService)}

}
