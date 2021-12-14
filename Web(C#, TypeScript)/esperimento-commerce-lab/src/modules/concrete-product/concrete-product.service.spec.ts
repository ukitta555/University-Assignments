import { Test, TestingModule } from '@nestjs/testing';
import { getRepositoryToken } from '@nestjs/typeorm';
import { Connection, Repository } from 'typeorm';
import { ConcreteProductOrmEntity } from './concrete-product.orm-entity';
import { ConcreteProductService } from './concrete-product.service';

describe('ConcreteProductService', () => {
  let service: ConcreteProductService;

  type MockRepository<T = any> = Partial<Record<keyof Repository<T>, jest.Mock>>


  beforeEach(async () => {
    const mockRepo = {
      find: jest.fn(() => ({}))
    }

    const module: TestingModule = await Test.createTestingModule({
      providers:
        [
          ConcreteProductService,
          { provide: getRepositoryToken(ConcreteProductOrmEntity), useValue: mockRepo },
          { provide: Connection, useValue: {}}
        ],
    }).compile();

    service = module.get<ConcreteProductService>(ConcreteProductService);
    // repository = module.get<MockRepository>(getRepositoryToken(ConcreteProductOrmEntity))
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });

});
