import useField from "../../hooks/useStringField"
import productService from "../../services/productService"
import { IConcreteProduct } from "./ProductCRUD"
import { Button, TextField, Box, Typography } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import { materialUIStyles, wrapperStyle } from "../../styles/styles"
import React from "react"

const useStyles = makeStyles(materialUIStyles);
const useInputStyles = makeStyles(materialUIStyles.input);

interface IProps {
  setProducts: (value: IConcreteProduct[] | ((prevVar: IConcreteProduct[]) => IConcreteProduct[])) => void,
  products: IConcreteProduct[],
}

const ProductDelete = ({ products, setProducts }: IProps) => {
  const classes = useStyles()
  const inputClasses = useInputStyles()
  const handleRemove = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    await productService.deleteProduct(Number(slug.value))
    setProducts(products.filter(
      product =>
        product.concreteProductId !== Number(slug.value)
    ))
  }

  const slug = useField('number')



  return (
    <div>
      <form onSubmit={handleRemove}>
        <Box style={wrapperStyle} textAlign="center">
          <Typography variant='h6' color='primary'> <b>DELETE request:</b> </Typography>
          <TextField inputProps={slug} InputProps={{ classes: inputClasses }} label='What product to remove' />
          <Button type='submit' className={classes.root}> Remove concrete product</Button>
        </Box>
      </form>
    </div>
  )
}

export default ProductDelete