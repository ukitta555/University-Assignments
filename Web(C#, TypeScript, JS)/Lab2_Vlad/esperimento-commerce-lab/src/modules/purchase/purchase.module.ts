import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { UserOrmEntity } from "../user/user.orm-entity";
import { PurchaseController } from './purchase.controller';
import { PurchaseOrmEntity } from "./purchase.orm-entity";
import { PurchaseService } from './purchase.service';

@Module({
 imports: [TypeOrmModule.forFeature([PurchaseOrmEntity, UserOrmEntity])],
 controllers: [PurchaseController],
 providers: [PurchaseService]
})
export class PurchaseModule {}