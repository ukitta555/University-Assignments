import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { ColorOrmEntity } from "./color.orm-entity";

@Injectable()
export class ColorService {
  constructor(
    @InjectRepository(ColorOrmEntity)
    private readonly colorRepo: Repository<ColorOrmEntity>
  ) {}

  async getAll() {
    return this.colorRepo.find({});
  }


  async createOne(color: any) {
    return this.colorRepo.save(color);
  }

  async updateOne(color: any, id: number) {
    return this.colorRepo.update(id, color)
  }

  async removeOne(id: number) {
    const colorToRemove = await this.colorRepo.findOne(id)
    return this.colorRepo.remove(colorToRemove)
  }
}