import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { UserOrmEntity } from "./user.orm-entity";
import { UsersController } from "./user.controller";
import { UsersService } from "./user.service";

@Module({
  imports: [TypeOrmModule.forFeature([UserOrmEntity])],
  controllers: [UsersController],
  providers: [UsersService],
})
export class UserModule {}