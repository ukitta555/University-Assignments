import { Injectable } from '@nestjs/common';
import { Repository } from 'typeorm';

@Injectable()
export class ServiceBase<Entity> {
  constructor(
    private readonly repo: Repository<Entity>
  ) {}

  async getAll() {
    const entries = await this.repo.find({})
    console.log(entries)
    return entries;
  }


  async createOne(entity: any) {
    return this.repo.save(entity);
  }

  async updateOne(entity: any, id: string) {
    return this.repo.save({ ...entity, concreteProductId: Number(id)})
  }

  async removeOne(id: number) {
    const entityToRemove = await this.repo.findOne(id)
    console.log(entityToRemove)
    return this.repo.remove(entityToRemove)
  }
}
