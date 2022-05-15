import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { ServiceBase } from 'src/core/service-base';
import { Repository } from 'typeorm/repository/Repository';
import { UserOrmEntity } from './user.orm-entity';

@Injectable()
export class UsersService extends ServiceBase<UserOrmEntity> {
  constructor(
    @InjectRepository(UserOrmEntity)
    private readonly userRepo: Repository<UserOrmEntity>
  ) {super(userRepo)}
}
