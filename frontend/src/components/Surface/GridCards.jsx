import { React } from 'react'
import PropTypes from 'prop-types'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import { Card, CardActionArea, CardContent, CardMedia, Grid, Typography } from '@mui/material'
import { Link } from 'react-router-dom'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function GridCards(props) {
  const { content } = props

  return (
    <Grid container style={{ marginLeft: '50px' }}>
      <ThemeProvider theme={darkTheme}>
        {content.map((item) => (
          <Grid key={item.key} size={{ xs: 1, sm: 6, md: 4 }} style={{ marginBottom: '80px' }}>
            <Card
              sx={{ minWidth: 240, maxWidth: 240, minHeight: 240, maxHeight: 240, borderRadius: 5, display: 'flex' }}
            >
              <CardActionArea
                component={Link}
                to={item.url_path}
                element={item.url_name}
                sx={{ display: 'flex', flexDirection: 'column' }}
              >
                <CardContent>
                  <Typography gutterBottom component='div'>
                    {item.title}
                  </Typography>
                </CardContent>
                <CardMedia
                  sx={{ border: 0, minWidth: 130, maxWidth: 130, minHeight: 130, maxHeight: 130 }}
                  component='img'
                  image={item.image}
                  alt={item.title}
                />
              </CardActionArea>
            </Card>
          </Grid>
        ))}
      </ThemeProvider>
    </Grid>
  )
}

GridCards.propTypes = {
  content: PropTypes.list,
}
