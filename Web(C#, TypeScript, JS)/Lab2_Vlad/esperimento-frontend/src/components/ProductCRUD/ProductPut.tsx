import useField from "../../hooks/useStringField"
import productService, { ProductDTO } from "../../services/productService"
import { IConcreteProduct } from "./ProductCRUD"
import { TextField, Button, Box, Typography } from '@material-ui/core'
import { materialUIStyles, wrapperStyle } from "../../styles/styles";
import { makeStyles } from '@material-ui/core/styles'

interface IProps {
  setProducts: (value: IConcreteProduct[] | ((prevVar: IConcreteProduct[]) => IConcreteProduct[])) => void,
  products: IConcreteProduct[],
}

const useStyles = makeStyles(materialUIStyles);

const useInputStyles = makeStyles(materialUIStyles.input);


const ProductPut = ({ products, setProducts }: IProps) => {
  const classes = useStyles()
  const inputClasses = useInputStyles()
  const slug = useField('number')
  const sizeId = useField('number')
  const colorId = useField('number')
  const productId = useField('number')
  const discountCodeId = useField('number')
  const price = useField('text')
  const amount = useField('number')
  const photoURL = useField('url')


  const handleUpdate = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const productToAdd: ProductDTO = {
      sizeId: Number(sizeId.value),
      colorId: Number(colorId.value),
      productId: Number(productId.value),
      discountCodeId: Number(discountCodeId.value),
      price: Number(price.value),
      amount: Number(amount.value),
      photoURL: photoURL.value
    }
    const updatedProduct = await productService.updateProduct(productToAdd, Number(slug.value))
    setProducts(products.map(
      product =>
        product.concreteProductId === Number(slug.value)
          ? updatedProduct
          : product
    ))
  }

  return (
    <div>

      <form onSubmit={handleUpdate}>
        <Box style={wrapperStyle} textAlign="center">
          <Typography variant='h6' color='primary'> <b>PUT request:</b> </Typography>
          <TextField inputProps={slug} InputProps={{ classes: inputClasses }} label = 'Conc. product ID'/>
          <TextField inputProps={sizeId} InputProps={{ classes: inputClasses }} label='Size ID'/>
          <TextField inputProps={colorId} InputProps={{ classes: inputClasses }} label = 'Color ID'/>
          <TextField inputProps={productId} InputProps={{ classes: inputClasses }} label = 'Product ID'/>
          <TextField inputProps={discountCodeId} InputProps={{ classes: inputClasses }} label = 'Discount code ID'/>
          <TextField inputProps={price} InputProps={{ classes: inputClasses }} label = 'Price'/>
          <TextField inputProps={amount} InputProps={{ classes: inputClasses }} label ='Amount'/>
          <TextField inputProps={photoURL} InputProps={{ classes: inputClasses }} label = 'Photo URL'/>
          <Button type='submit' className={classes.root}> Update concrete product</Button>
        </Box>
      </form>
    </div>
  )
}

export default ProductPut