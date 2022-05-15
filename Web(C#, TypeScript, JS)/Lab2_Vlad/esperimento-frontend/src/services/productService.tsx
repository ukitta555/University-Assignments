import axios from 'axios'
const baseURL = '/concrete-product'

export interface ProductDTO {
  sizeId: number,
  colorId: number,
  productId: number,
  discountCodeId: number,
  price: number,
  amount: number,
  photoURL: string
}

const getProducts = async () => {
  const response = await axios.get(baseURL)
  return response.data
}

const addProduct = async (productDTO: ProductDTO) => {
  const response = await axios.post(
    baseURL,
    productDTO
    )
  return response.data
}

const updateProduct = async (productDTO: ProductDTO, slug: number) => {
  const response = await axios.put(
    `${baseURL}/${slug}`,
    productDTO
  )
  return response.data
}

const deleteProduct = async (slug: number) => {
  await axios.delete(
    `${baseURL}/${slug}`
  )
}

const requests = {
  getProducts,
  addProduct,
  updateProduct,
  deleteProduct
}

export default requests