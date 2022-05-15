import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { ConcreteProductOrmEntity } from "../concrete-product.orm-entity";

@Entity("size")
export class SizeOrmEntity {
  @PrimaryGeneratedColumn()
  sizeId: number;

  @Column()
  sizeName: string;


  @OneToMany(() => ConcreteProductOrmEntity, concreteProduct => concreteProduct.sizeId)
  concreteProducts: ConcreteProductOrmEntity[]
}