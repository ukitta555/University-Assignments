import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CategoryController } from './category.controller';
import { CategoryOrmEntity } from './category.orm-entity';
import { CategoryService } from './category.service';

@Module({
  imports:[TypeOrmModule.forFeature([CategoryOrmEntity])],
  controllers: [CategoryController],
  providers: [CategoryService]
})
export class CategoryModule {}
