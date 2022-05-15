import { Controller } from '@nestjs/common';
import { ControllerBase } from 'src/core/controller-base';
import { PurchaseHistoryService } from './purchase-history.service';

@Controller('purchase-history')
export class PurchaseHistoryController extends ControllerBase{
  constructor(
    private readonly purchaseHistoryService: PurchaseHistoryService
  ) {super(purchaseHistoryService)}
}
