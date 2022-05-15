import { Body, Controller, Delete, Get, Param, Post, Put } from '@nestjs/common';
import { CollectionService } from './collection.service';

@Controller('collection')
export class CollectionController
{
  constructor(
    private readonly collectionService: CollectionService
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
