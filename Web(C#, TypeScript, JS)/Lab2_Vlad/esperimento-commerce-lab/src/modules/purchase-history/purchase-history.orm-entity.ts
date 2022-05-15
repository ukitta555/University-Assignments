import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from "typeorm";
import { ConcreteProductOrmEntity } from "../concrete-product/concrete-product.orm-entity";
import { PurchaseOrmEntity } from "../purchase/purchase.orm-entity";

@Entity('purchase_history')
export class PurchaseHistoryOrmEntity{
  @PrimaryGeneratedColumn()
  purchaseHistoryEntryId: number

  @ManyToOne(() => ConcreteProductOrmEntity, concreteProduct => concreteProduct.purchaseEntries, { onDelete: 'CASCADE' })
  concreteProduct: ConcreteProductOrmEntity

  @ManyToOne(() => PurchaseOrmEntity, purchase => purchase.purchaseEntries, { onDelete: 'CASCADE' })
  purchase: PurchaseOrmEntity

  @Column()
  amount: number
}