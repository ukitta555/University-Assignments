import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { typeOrmConfig } from './infrastructure/configs/typeorm.config';
import { DiscountCodeModule } from './modules/discount-code/discount-code.module';
import { ProductModule } from './modules/product/product.module';
import { PurchaseModule } from './modules/purchase/purchase.module';
import { UserModule } from './modules/user/user.module';
import { ConcereteProductModule } from './modules/concrete-product/concrete-product.module';
import { PurchaseHistoryModule } from './modules/purchase-history/purchase-history.module';

@Module({
  imports: [
    UserModule,
    PurchaseModule,
    DiscountCodeModule,
    ProductModule,
    ConcereteProductModule,
    PurchaseHistoryModule,
    TypeOrmModule.forRoot(typeOrmConfig)
  ],
  controllers: [],
  providers: [],
})
export class AppModule { }
