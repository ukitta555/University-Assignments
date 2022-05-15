import useField from "../../hooks/useStringField"
import productService, { ProductDTO } from "../../services/productService"
import { IConcreteProduct } from "./ProductCRUD"
import { TextField, Button, Box, Typography } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import { materialUIStyles, wrapperStyle } from "../../styles/styles"

interface IProps {
  setProducts: (value: IConcreteProduct[] | ((prevVar: IConcreteProduct[]) => IConcreteProduct[])) => void,
  products: IConcreteProduct[],
}


const useStyles = makeStyles(materialUIStyles);

const useInputStyles = makeStyles(materialUIStyles.input);

const ProductPost = ({ products, setProducts }: IProps) => {
  const classes = useStyles()
  const inputClasses = useInputStyles ()

  const sizeId = useField('number')
  const colorId = useField('number')
  const productId = useField('number')
  const discountCodeId = useField('number')
  const price = useField('text')
  const amount = useField('number')
  const photoURL = useField('url')


  const handleCreation = async (event: React.FormEvent<HTMLFormElement>) => {
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
    const addedProduct = await productService.addProduct(productToAdd)
    setProducts(products.concat(addedProduct))
  }

  return (
    <div>
      <form onSubmit={handleCreation}>
        <Box style={wrapperStyle} textAlign="center">
          <Typography variant='h6' color = 'primary'> <b>POST request:</b> </Typography>
          <TextField inputProps={sizeId} InputProps = {{classes: inputClasses}} color = 'secondary' label='Size ID'/>
          <TextField inputProps={colorId} InputProps={{ classes: inputClasses }} label='Color ID' />
          <TextField inputProps={productId} InputProps={{ classes: inputClasses }} label='Product ID' />
          <TextField inputProps={discountCodeId} InputProps={{ classes: inputClasses }} label='Discount ID' />
          <TextField inputProps={price} InputProps={{ classes: inputClasses }} label='Price' />
          <TextField inputProps={amount} InputProps={{ classes: inputClasses }} label='Amount' />
          <TextField inputProps={photoURL} InputProps={{ classes: inputClasses }} label='Photo URL' />
          <Button className={classes.root} type='submit'> Create new concrete product</Button>
        </Box>
      </form>
    </div>
  )
}

export default ProductPost