import { Controller } from '@nestjs/common';
import { ControllerBase } from '../../core/controller-base';
import { ConcreteProductService } from './concrete-product.service';

@Controller('concrete-product')
export class ConcreteProductController extends ControllerBase{
  constructor(
    private readonly concreteProductService: ConcreteProductService
  ) { super (concreteProductService)}
}
