import { Column, Entity,  ManyToOne,  OneToMany,  PrimaryGeneratedColumn } from "typeorm";
import { CategoryOrmEntity } from "../category/category.orm-entity";
import { CollectionOrmEntity } from "../collection/collection.orm-entity";
import { ConcreteProductOrmEntity } from "../concrete-product/concrete-product.orm-entity";

@Entity('discount_code')
export class DiscountCodeOrmEntity{
  @PrimaryGeneratedColumn()
  discountCodeId: number;

  @Column()
  code: string;

  @Column()
  discount: number;

  @ManyToOne(() => CollectionOrmEntity, collection => collection.discountCodes, { onDelete: 'CASCADE' })
  collection: number;

  @ManyToOne(() => CategoryOrmEntity, category => category.discountCodes, { onDelete: 'CASCADE' })
  category: number;


  @OneToMany(() => ConcreteProductOrmEntity, concreteProduct => concreteProduct.discountCodeId)
  concreteProducts: ConcreteProductOrmEntity[]
}