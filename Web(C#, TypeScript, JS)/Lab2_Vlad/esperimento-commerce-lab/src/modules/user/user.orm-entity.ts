import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { PurchaseOrmEntity } from "../purchase/purchase.orm-entity";

@Entity('user')
export class UserOrmEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column()
  surname: string;

  @Column()
  address: string;

  @Column()
  email: string;

  @Column()
  hashedPassword: string;

  @OneToMany(() => PurchaseOrmEntity, purchase => purchase.buyer)
  purchases: PurchaseOrmEntity[]
}
