import * as React from 'react';
import {createTheme, ThemeProvider} from "@mui/material/styles";
import {Card, CardActionArea, CardContent, CardMedia, Grid, Typography} from '@mui/material';
import {Link } from "react-router-dom";
import ListConsumables from "./Consumables/ListConsumables";
import ListAccessories from "./Accessories/ListAccessories";
import ListConsumablesCategory from "./ConsumablesCategories/ListConsumablesCategory";
import ListAccessoriesCategory from "./AccessoriesCategories/ListAccessoriesCategory";


const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const ConsumablesContent = [
    {'title': 'Расходники', 'url_path': '/consumables/list', 'url_name': ListConsumables, 'image': 'http://localhost/static/images/consumables.svg'},
    {'title': 'Группы расходников', 'url_path': '/consumables/categories/list', 'url_name': ListConsumablesCategory, 'image': 'http://localhost/static/images/post.svg'},
    {'title': 'Комплектующие', 'url_path': '/accessories/list', 'url_name': ListAccessories, 'image': 'http://localhost/static/images/accessories.svg'},
    {'title': 'Группы комплектующих', 'url_path': '/accessories/categories/list', 'url_name': ListAccessoriesCategory, 'image': 'http://localhost/static/images/post.svg'},
];
export {ConsumablesContent}

const IndexConsumables = () => {
    return (
        <Grid container style={{marginLeft: "50px"}}>
            <ThemeProvider theme={darkTheme}>
                {ConsumablesContent.map((item) => (
                    <Grid item xs={12} sm={6} md={4} style={{marginBottom: "80px"}}>
                        <Card sx={{minWidth: 200, maxWidth: 200, minHeight: 200, maxHeight: 200, borderRadius: 5,
                            display: 'flex'}}>
                            <CardActionArea component={Link} to={item.url_path} element={item.url_name}
                                            sx={{ display: 'flex', flexDirection: 'column' }}>
                                <CardContent>
                                    <Typography gutterBottom   component="div">
                                        {item.title}
                                    </Typography>
                                </CardContent>
                                <CardMedia
                                    sx={{ border: 0, minWidth: 120, maxWidth: 120, minHeight: 120, maxHeight: 120,}}
                                    component="img"
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

export default IndexConsumables;