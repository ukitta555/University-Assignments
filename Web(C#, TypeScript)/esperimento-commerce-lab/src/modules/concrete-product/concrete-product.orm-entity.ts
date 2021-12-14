import { Column, Entity, ManyToOne, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { ColorOrmEntity } from "./color/color.orm-entity";
import { DiscountCodeOrmEntity } from "../discount-code/discount-code.orm-entity";
import { ProductOrmEntity } from "../product/product.orm-entity";
import { PurchaseHistoryOrmEntity } from "../purchase-history/purchase-history.orm-entity";
import { SizeOrmEntity } from "./size/size.orm-entity";

@Entity("concrete_product")
export class ConcreteProductOrmEntity{
  @PrimaryGeneratedColumn()
  concreteProductId: number

  @ManyToOne(() => ProductOrmEntity, product => product.concreteProducts, { onDelete: 'CASCADE' })
  productId: ProductOrmEntity

  @ManyToOne(() => SizeOrmEntity, size => size.concreteProducts, { onDelete: 'CASCADE' })
  sizeId: SizeOrmEntity

  @ManyToOne(() => ColorOrmEntity, color => color.concreteProducts, { onDelete: 'CASCADE' })
  colorId: ColorOrmEntity

  @ManyToOne(() => DiscountCodeOrmEntity, discount => discount.concreteProducts, { onDelete: 'CASCADE' })
  discountCodeId: DiscountCodeOrmEntity

  @OneToMany(() => PurchaseHistoryOrmEntity, purchaseEntry => purchaseEntry.concreteProduct)
  purchaseEntries: PurchaseHistoryOrmEntity[]

  @Column()
  price: number

  @Column()
  amount: number

  @Column()
  photoURL: string;
}