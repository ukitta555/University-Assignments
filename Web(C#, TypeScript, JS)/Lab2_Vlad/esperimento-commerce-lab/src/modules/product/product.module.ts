import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { CategoryModule } from "../category/category.module";
import { CollectionModule } from "../collection/collection.module";
import { ProductOrmEntity } from "./product.orm-entity";
import { ProductService } from './product.service';
import { ProductController } from './product.controller';

@Module({
 imports: [TypeOrmModule.forFeature([ProductOrmEntity]), CategoryModule, CollectionModule],
 controllers: [ProductController],
 providers: [ProductService]
})
export class ProductModule {}