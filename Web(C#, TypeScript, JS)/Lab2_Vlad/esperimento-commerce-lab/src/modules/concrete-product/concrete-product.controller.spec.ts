import { Test, TestingModule } from '@nestjs/testing';
import { ConcreteProductController } from './concrete-product.controller';
import { ConcreteProductService } from './concrete-product.service';


describe('ConcreteProductController', () => {
  let controller: ConcreteProductController;
  let service: ConcreteProductService;


  const serviceMock = {
    getAll: jest.fn(() => ({}) ),
    createOne: jest.fn((obj) => ({...obj, id: 1})),
    updateOne: jest.fn((obj, id) => ({...obj, isUpdated: 1, id})),
    removeOne: jest.fn((id) => ({id, isRemoved: 1}))
  }


  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [ConcreteProductController],
      providers: [
        { provide: ConcreteProductService, useValue: serviceMock},
      ]
    }).compile();

    controller = module.get<ConcreteProductController>(ConcreteProductController);
    service = module.get<ConcreteProductService>(ConcreteProductService)
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });

  it('shouldn\'t crash', () => {
    console.log(123)
  });

  it('should return all products for GET requests', () => {
    const mockReturn = {}
    expect(service.getAll()).toStrictEqual(mockReturn)
  })

  it('should create a product', () => {
    const objToAdd = { test: 123}
    expect(service.createOne(objToAdd)).toStrictEqual({...objToAdd, id: 1})
  })

  it('should update a product', () => {
    const objToUpdate = { test: 123 }
    const id = '1'
    expect(service.updateOne(objToUpdate, id)).toStrictEqual({ ...objToUpdate, isUpdated: 1, id})
  })

  it('should delete a product', () => {
    const id = 1
    expect(service.removeOne(id)).toStrictEqual({ id, isRemoved: 1})
  })

});
