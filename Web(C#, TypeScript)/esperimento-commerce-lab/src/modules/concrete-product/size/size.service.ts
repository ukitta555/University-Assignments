import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { SizeOrmEntity } from "./size.orm-entity";

@Injectable()
export class SizeService {
  constructor(
    @InjectRepository(SizeOrmEntity)
    private readonly sizeRepository: Repository<SizeOrmEntity>
  ) {}

  async getAll() {
    const sizes = await this.sizeRepository.find({})
    return sizes
  }

  async createOne(size: any) {
    const sizeInDB = await this.sizeRepository.save(size)
    return sizeInDB
  }

  async updateOne(size: any, id: number) {
    const updatedSize = await this.sizeRepository.update(id, size)
    return updatedSize
  }

  async removeOne(id: number) {
    const size = await this.sizeRepository.findOne(id)
    await this.sizeRepository.remove(size)
    return ;
  }
}