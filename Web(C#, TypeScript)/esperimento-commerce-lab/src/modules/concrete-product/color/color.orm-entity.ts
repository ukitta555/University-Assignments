import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { ConcreteProductOrmEntity } from "../concrete-product.orm-entity";

@Entity("color")
export class ColorOrmEntity {
  @PrimaryGeneratedColumn()
  colorId: number;

  @Column()
  colorName: string;

  @OneToMany(() => ConcreteProductOrmEntity, concreteProduct => concreteProduct.colorId)
  concreteProducts: ConcreteProductOrmEntity[]
}