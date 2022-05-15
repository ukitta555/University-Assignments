import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { DiscountCodeOrmEntity } from "../discount-code/discount-code.orm-entity";
import { ProductOrmEntity } from "../product/product.orm-entity";

@Entity('category')
export class CategoryOrmEntity {
  @PrimaryGeneratedColumn()
  categoryId: number;

  @Column()
  categoryName: string;

  @OneToMany(() => DiscountCodeOrmEntity, discountCode => discountCode.category)
  discountCodes: number[];

  @OneToMany(() => ProductOrmEntity, product => product.category)
  products: ProductOrmEntity[];

}