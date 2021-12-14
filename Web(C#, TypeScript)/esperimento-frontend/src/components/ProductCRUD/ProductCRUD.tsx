import React, { useState } from 'react'
import ProductDelete from './ProductDelete'
import ProductGet from './ProductGet'
import ProductPost from './ProductPost'
import ProductPut from './ProductPut'

interface ISize {
  sizeId: number,
  sizeName: string
}

interface IProduct {
  productId: number,
  description: string,
}

interface IColor {
  colorId: number,
  colorName: string
}

interface IDiscount {
  discountId: number,
  code: string,
  discount: number
}

export interface IConcreteProduct {
  concreteProductId: number,
  price: number,
  amount: number,
  photoURL: string,
  sizeId: ISize,
  productId: IProduct,
  colorId: IColor,
  discountId: IDiscount
}

const ProductCRUD = () => {
  const [products, setProducts] = useState<IConcreteProduct[]>([])
  const [areProductsHidden, setAreProductsHidden] = useState<boolean>(true)

  return (
    <div>

      <ProductGet
        areProductsHidden={areProductsHidden}
        setAreProductsHidden={setAreProductsHidden}
        products={products}
        setProducts={setProducts}
      />
      <ProductPost
        products={products}
        setProducts={setProducts}
      />

      <ProductPut
        products = {products}
        setProducts = {setProducts}
      />

      <ProductDelete
        products={products}
        setProducts={setProducts}
      />
    </div>
  )
}

export default ProductCRUD