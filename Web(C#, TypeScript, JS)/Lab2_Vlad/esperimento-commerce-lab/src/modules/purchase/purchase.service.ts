import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { ServiceBase } from 'src/core/service-base';
import { Repository } from 'typeorm';
import { PurchaseOrmEntity } from './purchase.orm-entity';

@Injectable()
export class PurchaseService extends ServiceBase<PurchaseOrmEntity> {
  constructor(
    @InjectRepository(PurchaseOrmEntity)
    private readonly purchaseRepo: Repository<PurchaseOrmEntity>
  ) {super(purchaseRepo)}

  async getAll(){
    return await this.purchaseRepo
      .createQueryBuilder('purchase')
      .leftJoinAndSelect('purchase.buyer', 'user')
      .getMany();
  }
}
