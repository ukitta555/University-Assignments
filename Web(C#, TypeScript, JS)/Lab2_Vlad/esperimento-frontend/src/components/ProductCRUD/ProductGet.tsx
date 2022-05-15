import React from 'react'
import productService from '../../services/productService'
import { IConcreteProduct } from './ProductCRUD'
import { makeStyles } from '@material-ui/core/styles'
import { CardMedia, Button, Box, Typography, Card, CardContent, CardActionArea } from '@material-ui/core'
import { materialUIStyles, wrapperStyle } from '../../styles/styles'

interface IProps {
  setProducts: (value: IConcreteProduct[] | ((prevVar: IConcreteProduct[]) => IConcreteProduct[])) => void,
  products: IConcreteProduct[],
  setAreProductsHidden: (value: boolean | ((prevVar: boolean) => boolean)) => void,
  areProductsHidden: boolean
}

interface ProductProps {
  product: IConcreteProduct
}

const useStyles = makeStyles(materialUIStyles);


const ProductComponent = ({ product }: ProductProps) => {
  const classes = useStyles()
  return (
    <Card style= {{margin: 10}} >
      <CardActionArea >
        <CardMedia image={product.photoURL} style={{
          height: 0,
          paddingTop: '56.25%'
        }} />
        <CardContent className={classes.card}>
          <Typography variant='h6'> Price: {product.price} </Typography>
          <Typography variant='h6'> Amount: {product.amount} </Typography>
          <Typography variant='h6'> ID: {product.concreteProductId} </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  )
}


const ProductGet = ({ products, setProducts, areProductsHidden, setAreProductsHidden }: IProps) => {
  const classes = useStyles()

  const handleGetButtonClick = async (event: React.MouseEvent<HTMLButtonElement>) => {
    const products: IConcreteProduct[] = await productService.getProducts()
    setProducts(products)
    setAreProductsHidden(false)
  }


  const productsStyles = areProductsHidden ? { display: 'none' } : { display: 'block' }

  return (
    <Box style={wrapperStyle}>
      <Button onClick={handleGetButtonClick} className={classes.root}> Get Data </Button>
      <Box style={productsStyles}>
        {
          products.map((product: IConcreteProduct) =>
            <ProductComponent key={product.concreteProductId} product={product} />
          )
        }
      </Box>
    </Box>
  )
}

export default ProductGet