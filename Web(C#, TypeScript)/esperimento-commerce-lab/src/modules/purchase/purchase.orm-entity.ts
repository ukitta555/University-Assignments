import { Column, Entity, ManyToOne, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { PurchaseHistoryOrmEntity } from "../purchase-history/purchase-history.orm-entity";
import { UserOrmEntity } from "../user/user.orm-entity";

enum ProductStatusEnum {
  Liked,
  AddedToCart,
  Bought
}

@Entity("purchase")
export class PurchaseOrmEntity {
  @PrimaryGeneratedColumn()
  purchaseId: number;

  @Column({type: "timestamptz"})
  date: Date;

  @Column('enum',{name:'product_status', enum: ProductStatusEnum })
  status: ProductStatusEnum;

  @ManyToOne(() => UserOrmEntity, user => user.purchases, { onDelete: 'CASCADE' })
  buyer: UserOrmEntity;

  @OneToMany(() => PurchaseHistoryOrmEntity, purchaseEntry => purchaseEntry.purchase)
  purchaseEntries: PurchaseHistoryOrmEntity[]

}