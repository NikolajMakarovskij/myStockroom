import * as React from 'react';
import IndexWorkplace from "../appWorkplace/IndexWorkplace";
import {createTheme, ThemeProvider} from "@mui/material/styles";
import {Card, CardActionArea, CardContent, CardMedia, Grid, Typography} from '@mui/material';
import {Link } from "react-router-dom";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const HomeContent = [
    {'title': "Склад", 'url_path': '/stock', 'url_name': 'core:index', 'image': 'http://localhost/static/images/warehouse.svg'},
    {'title': "Расходники", 'url_path': '/consumables', 'url_name': 'core:index', 'image': 'http://localhost/static/images/consumables.svg'},
    {'title': "Контрагенты", 'url_path': '/counterparty', 'url_name': 'core:index', 'image': 'http://localhost/static/images/post.svg'},
    {'title': "Рабочие места", 'url_path': '/workplace', 'url_name': IndexWorkplace, 'image': 'http://localhost/static/images/workplace.svg'},
    {'title': "Устройства", 'url_path': '/device', 'url_name': 'core:index', 'image': 'http://localhost/static/images/device.svg'},
    {'title': "Софт", 'url_path': '/software', 'url_name': 'core:index', 'image': 'http://localhost/static/images/software.svg'},
    {'title': "ЭЦП", 'url_path': '/signature', 'url_name': 'core:index', 'image': 'http://localhost/static/images/signature.svg'},
    {'title': "Сотрудники", 'url_path': '/employee', 'url_name': 'core:index', 'image': 'http://localhost/static/images/employee.svg'},

];


const Home = () => {
    return (
        <Grid container style={{marginLeft: "50px"}}>
            <ThemeProvider theme={darkTheme}>
                {HomeContent.map((item) => (
                    <Grid item xs={12} sm={6} md={4} style={{marginBottom: "80px"}}>
                        <Card sx={{minWidth: 200, maxWidth: 200, minHeight: 200, maxHeight: 200, borderRadius: 5}}>
                            <CardActionArea component={Link} to={item.url_path} element={item.url_name}>
                                <CardContent>
                                    <Typography gutterBottom   component="div">
                                        {item.title}
                                    </Typography>
                                </CardContent>
                                <CardMedia
                                    sx={{ border: 0 }}
                                    component="iframe"
                                    height="140px"
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

export default Home;