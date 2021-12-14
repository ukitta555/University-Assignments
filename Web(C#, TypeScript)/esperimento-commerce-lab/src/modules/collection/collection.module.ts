import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CollectionController } from './collection.controller';
import { CollectionOrmEntity } from './collection.orm-entity';
import { CollectionService } from './collection.service';

@Module({
  imports: [TypeOrmModule.forFeature([CollectionOrmEntity])],
  controllers: [CollectionController],
  providers: [CollectionService]
})
export class CollectionModule {}
