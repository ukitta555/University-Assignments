import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { DiscountCodeOrmEntity } from './discount-code.orm-entity';

@Injectable()
export class DiscountCodeService {
  constructor(
    @InjectRepository(DiscountCodeOrmEntity)
    private readonly discountCodeRepo: Repository<DiscountCodeOrmEntity>
  ) {}

  async getAll() {
      return await this.discountCodeRepo
        .createQueryBuilder('discount_code')
        .leftJoinAndSelect('discount_code.collection', 'collection')
        .leftJoinAndSelect('discount_code.category', 'category')
        .getMany();
  }


  async createOne(collection: any) {
    return this.discountCodeRepo.save(collection);
  }

  async updateOne(collection: any, id: number) {
    return this.discountCodeRepo.update(id, collection)
  }

  async removeOne(id: number) {
    const codeToRemove = await this.discountCodeRepo.findOne(id)
    return this.discountCodeRepo.remove(codeToRemove)
  }
}
