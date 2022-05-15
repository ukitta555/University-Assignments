import { Body, Controller, Delete, Get, Param, Post, Put } from "@nestjs/common";
import { CategoryService } from "./category.service";

@Controller('category')
export class CategoryController {
  constructor(
    private readonly categoryService: CategoryService
  ) { }

  @Get()
  async getAll() {
    return this.categoryService.getAll()
  }

  @Post()
  async createOne(@Body() category: any) {
    return this.categoryService.createOne(category)
  }

  @Put(':id')
  async updateOne(@Body() category: any, @Param('id') id: number) {
    return this.categoryService.updateOne(category, id)
  }

  @Delete(':id')
  async deleteOne(@Param('id') id: number) {
    return this.categoryService.removeOne(id)
  }
}