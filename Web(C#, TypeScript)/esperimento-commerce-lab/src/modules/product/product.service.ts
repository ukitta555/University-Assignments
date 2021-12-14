import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { ServiceBase } from 'src/core/service-base';
import { Repository } from 'typeorm';
import { ProductOrmEntity } from './product.orm-entity';

@Injectable()
export class ProductService extends ServiceBase<ProductOrmEntity>{
  constructor(
    @InjectRepository(ProductOrmEntity)
    private readonly productRepo: Repository<ProductOrmEntity>
  ) { super(productRepo) }

  async getAll(){
    return await this.productRepo
      .createQueryBuilder('product')
      .leftJoinAndSelect('product.collection', 'collection')
      .leftJoinAndSelect('product.category', 'category')
      .getMany();
  }
}
