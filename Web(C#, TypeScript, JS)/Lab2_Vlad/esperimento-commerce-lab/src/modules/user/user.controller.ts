import { Controller } from '@nestjs/common';
import { ControllerBase } from 'src/core/controller-base';
import { UsersService } from './user.service';

@Controller('user')
export class UsersController extends ControllerBase {
  constructor(
    private readonly userService: UsersService
  ) {super(userService)}
}
