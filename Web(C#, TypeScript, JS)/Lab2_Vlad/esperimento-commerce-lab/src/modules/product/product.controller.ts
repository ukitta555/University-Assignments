import { Controller } from '@nestjs/common';
import { ControllerBase } from 'src/core/controller-base';
import { ProductService } from './product.service';

@Controller('product')
export class ProductController extends ControllerBase
{
  constructor(
    private readonly productService: ProductService
  ) { super(productService) }
}
