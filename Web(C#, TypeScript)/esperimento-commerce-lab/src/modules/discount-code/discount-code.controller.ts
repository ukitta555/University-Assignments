import { Body, Controller, Delete, Get, Param, Post, Put } from '@nestjs/common';
import { DiscountCodeService } from './discount-code.service';

@Controller('discount-code')
export class DiscountCodeController
{

  constructor(
    private readonly collectionService: DiscountCodeService
  ) { }

  @Get()
  async getAll()
  {
    return this.collectionService.getAll()
  }

  @Post()
  async createOne(@Body() collection: any)
  {
    return this.collectionService.createOne(collection)
  }

  @Put(':id')
  async updateOne(@Body() collection: any, @Param('id') id: number)
  {
    return this.collectionService.updateOne(collection, id)
  }

  @Delete(':id')
  async deleteOne(@Param('id') id: number)
  {
    return this.collectionService.removeOne(id)
  }

}
