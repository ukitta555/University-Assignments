import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { ServiceBase } from '../../core/service-base';
import { Repository } from 'typeorm';
import { ConcreteProductOrmEntity } from './concrete-product.orm-entity';

@Injectable()
export class ConcreteProductService extends ServiceBase<ConcreteProductOrmEntity> {
  constructor (
    @InjectRepository(ConcreteProductOrmEntity)
    private readonly concreteProductRepo: Repository<ConcreteProductOrmEntity>
  ) {super(concreteProductRepo)}

  async getAll(){
    return await this.concreteProductRepo
      .createQueryBuilder('concrete_product')
      .leftJoinAndSelect('concrete_product.sizeId', 'size')
      .leftJoinAndSelect('concrete_product.productId', 'product')
      .leftJoinAndSelect('concrete_product.colorId', 'color')
      .leftJoinAndSelect('concrete_product.discountCodeId', 'discount_code')
      .getMany();
  }

  async createOne(entity: any) {
    const result = await this.concreteProductRepo.save(entity);
    return await this.concreteProductRepo
      .createQueryBuilder('concrete_product')
      .leftJoinAndSelect('concrete_product.sizeId', 'size')
      .leftJoinAndSelect('concrete_product.productId', 'product')
      .leftJoinAndSelect('concrete_product.colorId', 'color')
      .leftJoinAndSelect('concrete_product.discountCodeId', 'discount_code')
      .where('concrete_product.concreteProductId = :id', {id: result.concreteProductId})
      .getOne()
  }

  async updateOne(entity: any, id: string) {
    const result = await this.concreteProductRepo.save({ ...entity, concreteProductId: Number(id) })
    return await this.concreteProductRepo
      .createQueryBuilder('concrete_product')
      .leftJoinAndSelect('concrete_product.sizeId', 'size')
      .leftJoinAndSelect('concrete_product.productId', 'product')
      .leftJoinAndSelect('concrete_product.colorId', 'color')
      .leftJoinAndSelect('concrete_product.discountCodeId', 'discount_code')
      .where('concrete_product.concreteProductId = :id', { id: result.concreteProductId })
      .getOne()
  }
}
