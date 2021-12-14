import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { PurchaseHistoryOrmEntity } from './purchase-history.orm-entity';
import { PurchaseHistoryService } from './purchase-history.service';
import { PurchaseHistoryController } from './purchase-history.controller';

@Module({
  imports: [TypeOrmModule.forFeature([PurchaseHistoryOrmEntity])],
  controllers: [PurchaseHistoryController],
  providers: [PurchaseHistoryService]
})
export class PurchaseHistoryModule {}
