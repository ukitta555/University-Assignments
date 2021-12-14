import { Delete, Put } from "@nestjs/common";
import { Body, Controller, Get, Param, Post } from "@nestjs/common";
import { ColorService } from "./color.service";

@Controller('color')
export class ColorController
{
  constructor(
    private readonly colorService: ColorService
  ) { }
  @Get()
  async getAll() {
    return this.colorService.getAll()
  }

  @Post()
  async createOne(@Body() color: any) {
    return this.colorService.createOne(color)
  }

  @Put(':id')
  async updateOne(@Body() color: any, @Param('id') id: number) {
    return this.colorService.updateOne(color, id)
  }

  @Delete(':id')
  async deleteOne(@Param('id') id: number) {
    return this.colorService.removeOne(id)
  }
}