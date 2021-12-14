import { createMuiTheme } from '@material-ui/core/styles';
import red from '@material-ui/core/colors/red';
import deepOrange from '@material-ui/core/colors/deepOrange';
import { CSSProperties } from 'react';

export const theme = createMuiTheme({
  palette: {
    primary: {
      main: 'rgba(255,255,255,0.9)',
    },
    secondary: {
      main: 'rgba(255,255,255,0.9)',
    },
    text: {
      primary: 'rgba(255,255,255,0.9)',
      secondary: 'rgba(255,255,255,0.65)'
    },
  }
});



export const materialUIStyles = {
  root: {
    background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
    border: 0,
    borderRadius: 3,
    boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
    color: 'white',
    height: 48,
    padding: '0 30px',
  },
  card: {
    background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
  },
  input: {
    focused: {},
    disabled: {},
    error: {},
    underline: {
      "&:before": {
        borderBottom: "2px solid rgba(255,255,255,0.5)"
      },
    },
  }
}

export const wrapperStyle: CSSProperties = {
  display: 'flex',
  flexDirection: 'column',
  width: '35vw',
  marginLeft: 'auto',
  marginRight: 'auto',
  marginTop: '2vh',
  marginBottom: '2vh',
}