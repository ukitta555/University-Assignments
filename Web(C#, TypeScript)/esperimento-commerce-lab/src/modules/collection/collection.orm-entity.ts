import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { DiscountCodeOrmEntity } from "../discount-code/discount-code.orm-entity";
import { ProductOrmEntity } from "../product/product.orm-entity";

@Entity("collection")
export class CollectionOrmEntity {
  @PrimaryGeneratedColumn()
  collectionId: number;

  @Column()
  collectionName: string;

  @OneToMany(() => DiscountCodeOrmEntity, discountCode => discountCode.collection)
  discountCodes: number[]

  @OneToMany(() => ProductOrmEntity, product => product.collection)
  products: ProductOrmEntity[];
}