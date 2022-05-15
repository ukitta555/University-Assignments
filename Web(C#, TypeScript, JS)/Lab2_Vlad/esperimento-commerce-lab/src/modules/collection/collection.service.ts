import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { CollectionOrmEntity } from "./collection.orm-entity";

@Injectable()
export class CollectionService {
  constructor(
    @InjectRepository(CollectionOrmEntity)
    private readonly collectionRepo: Repository<CollectionOrmEntity>
  ) {}

  async getAll() {
    return this.collectionRepo.find({});
  }


  async createOne(collection: any) {
    return this.collectionRepo.save(collection);
  }

  async updateOne(collection: any, id: number) {
    return this.collectionRepo.update(id, collection)
  }

  async removeOne(id: number) {
    const collectionToRemove = await this.collectionRepo.findOne(id)
    return this.collectionRepo.remove(collectionToRemove)
  }
}