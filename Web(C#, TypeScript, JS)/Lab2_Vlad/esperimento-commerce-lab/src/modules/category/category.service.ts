import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { CategoryOrmEntity } from "./category.orm-entity";

@Injectable()
export class CategoryService {
  constructor(
    @InjectRepository(CategoryOrmEntity)
    private readonly categoryRepo: Repository<CategoryOrmEntity>
  ) {}

  async getAll() {
    return this.categoryRepo.find({});
  }


  async createOne(category: any) {
    return this.categoryRepo.save(category);
  }

  async updateOne(category: any, id: number) {
    return this.categoryRepo.update(id, category)
  }

  async removeOne(id: number) {
    const categoryToRemove = await this.categoryRepo.findOne(id)
    return this.categoryRepo.remove(categoryToRemove)
  }
}