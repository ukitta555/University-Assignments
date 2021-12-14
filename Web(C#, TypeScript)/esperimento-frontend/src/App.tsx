import React from 'react';
import ProductCRUD from './components/ProductCRUD/ProductCRUD';
import { theme } from './styles/styles';
import { ThemeProvider } from '@material-ui/styles'
import { Box } from '@material-ui/core'
import background from './images/bg4.jpg'

function App() {
  return (
    <Box style={{ backgroundImage: `url(${background})`, backgroundSize: '100% 100%', opacity: '0.9' }}>
      <ThemeProvider theme={theme} >
        <ProductCRUD />
      </ThemeProvider>
    </Box>
  );
}

export default App;
