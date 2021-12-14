import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { ServiceBase } from 'src/core/service-base';
import { Repository } from 'typeorm';
import { PurchaseHistoryOrmEntity } from './purchase-history.orm-entity';

@Injectable()
export class PurchaseHistoryService extends ServiceBase<PurchaseHistoryOrmEntity>{
  constructor(
    @InjectRepository(PurchaseHistoryOrmEntity)
    private readonly purchaseHistoryRepo: Repository<PurchaseHistoryOrmEntity>
  ) {super(purchaseHistoryRepo)}


  async getAll(){
    return await this.purchaseHistoryRepo
      .createQueryBuilder('purchase_history')
      .leftJoinAndSelect('purchase_history.concreteProduct', 'concrete_product')
      .leftJoinAndSelect('purchase_history.purchase', 'purchase')
      .getMany();
  }
}
