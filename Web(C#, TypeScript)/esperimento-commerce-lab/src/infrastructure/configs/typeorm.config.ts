import { TypeOrmModuleOptions } from '@nestjs/typeorm'
import { config } from 'dotenv'

config()

export const typeOrmConfig: TypeOrmModuleOptions = {
  type: 'postgres',
  host: 'localhost',
  port: Number(process.env.DB_PORT) ,
  username: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  autoLoadEntities: true,
  synchronize: true
}