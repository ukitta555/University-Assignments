import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm/dist/typeorm.module";
import { CategoryModule } from "../category/category.module";
import { CollectionModule } from "../collection/collection.module";
import { DiscountCodeOrmEntity } from "./discount-code.orm-entity";
import { DiscountCodeService } from './discount-code.service';
import { DiscountCodeController } from './discount-code.controller';

@Module({
  imports: [TypeOrmModule.forFeature([DiscountCodeOrmEntity]), CategoryModule, CollectionModule],
  controllers: [DiscountCodeController],
  providers: [DiscountCodeService]
 })
 export class DiscountCodeModule {}