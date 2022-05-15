import { Body, Delete, Get, Param, Post, Put } from '@nestjs/common';

interface IService {
  getAll: () => Promise<any>,
  createOne: (entity: any) => Promise<any>,
  updateOne: (entity: any, id: string) => Promise<any>
  removeOne: (id: number) => Promise<any>
}

export class ControllerBase
{
  constructor(
    private readonly service: IService
  ) { }

  @Get()
  async getAll()
  {
    return this.service.getAll()
  }

  @Post()
  async createOne(@Body() collection: any)
  {
    return this.service.createOne(collection)
  }

  @Put(':id')
  async updateOne(@Body() entity: any, @Param('id') id: string)
  {
    return this.service.updateOne(entity, id)
  }

  @Delete(':id')
  async deleteOne(@Param('id') id: number)
  {
    console.log(id)
    return this.service.removeOne(id)
  }

}
