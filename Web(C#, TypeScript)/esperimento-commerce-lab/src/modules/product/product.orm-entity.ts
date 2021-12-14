import { Column, Entity, ManyToOne, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { CategoryOrmEntity } from "../category/category.orm-entity";
import { CollectionOrmEntity } from "../collection/collection.orm-entity";
import { ConcreteProductOrmEntity } from "../concrete-product/concrete-product.orm-entity";

@Entity("product")
export class ProductOrmEntity {
  @PrimaryGeneratedColumn()
  productId: number;

  @Column()
  description: string;


  @ManyToOne(() => CategoryOrmEntity, category => category.products, { onDelete: 'CASCADE' })
  category: CategoryOrmEntity;

  @ManyToOne(() => CollectionOrmEntity, collection => collection.products, { onDelete: 'CASCADE' })
  collection: CategoryOrmEntity;


  @OneToMany(() => ConcreteProductOrmEntity, concreteProduct => concreteProduct.productId)
  concreteProducts: ConcreteProductOrmEntity[]
}