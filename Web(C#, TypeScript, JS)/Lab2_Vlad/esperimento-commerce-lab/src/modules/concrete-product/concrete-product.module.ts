import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ColorController } from './color/color.controller';
import { ColorOrmEntity } from './color/color.orm-entity';
import { ColorService } from './color/color.service';
import { SizeController } from './size/size.controller';
import { SizeOrmEntity } from './size/size.orm-entity';
import { SizeService } from './size/size.service';
import { ConcreteProductOrmEntity } from './concrete-product.orm-entity';
import { ConcreteProductService } from './concrete-product.service';
import { ConcreteProductController } from './concrete-product.controller';

@Module({
  imports: [TypeOrmModule.forFeature([ConcreteProductOrmEntity, SizeOrmEntity, ColorOrmEntity])],
  controllers: [SizeController, ColorController, ConcreteProductController],
  providers: [SizeService, ColorService, ConcreteProductService]
})
export class ConcereteProductModule {}
