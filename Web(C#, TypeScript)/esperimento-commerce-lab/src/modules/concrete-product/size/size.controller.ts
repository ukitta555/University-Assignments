import { Body, Controller, Delete, Get, Param, Post, Put } from '@nestjs/common';
import { SizeService } from './size.service';

@Controller('size')
export class SizeController {
  constructor(
    private readonly sizeService: SizeService
  ) {}

  @Get()
  getAll() {
    return this.sizeService.getAll()
  }

  @Post()
  createOne(@Body() body) {
    console.log(body)
    return this.sizeService.createOne(body)
  }

  @Put(':id')
  updateOne(@Body() body, @Param('id') id: number) {
    return this.sizeService.updateOne(body, id)
  }

  @Delete(':id')
  deleteOne(@Param('id') id: number) {
    this.sizeService.removeOne(id);
  }
}
