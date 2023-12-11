import * as React from 'react';
import Card from '@mui/material/Card';
import Grid from '@mui/material/Grid';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import HomeWorkplace from "../appWorkplace/HomeWorkplace";
import {createTheme, ThemeProvider} from "@mui/material/styles";
import { CardActionArea } from '@mui/material';
import {Route, Link} from "@mui/icons-material";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const HomeContent = [
    {'title': "Склад", 'url_path': '/stock', 'url_name': 'core:index', 'image': 'http://172.18.0.9/static/images/warehouse.svg'},
    {'title': "Расходники", 'url_path': '/consumables', 'url_name': 'core:index', 'image': 'http://172.18.0.9/static/images/consumables.svg'},
    {'title': "Контрагенты", 'url_path': '/counterparty', 'url_name': 'core:index', 'image': 'http://172.18.0.9/static/images/post.svg'},
    {'title': "Рабочие места", 'url_path': '/workplace', 'url_name': HomeWorkplace, 'image': 'http://172.18.0.9/static/images/workplace.svg'},
    {'title': "Устройства", 'url_path': '/device', 'url_name': 'core:index', 'image': 'http://172.18.0.9/static/images/device.svg'},
    {'title': "Софт", 'url_path': '/software', 'url_name': 'core:index', 'image': 'http://172.18.0.9/static/images/software.svg'},
    {'title': "ЭЦП", 'url_path': '/signature', 'url_name': 'core:index', 'image': 'http://172.18.0.9/static/images/signature.svg'},
    {'title': "Сотрудники", 'url_path': '/employee', 'url_name': 'core:index', 'image': 'http://172.18.0.9/static/images/employee.svg'},

];


const Home = () => {
    return (
        <Grid container style={{marginLeft: "50px"}}>
            <ThemeProvider theme={darkTheme}>
                {HomeContent.map((item) => (
                    <Grid item xs={12} sm={6} md={4} style={{marginTop: "80px"}}>

                        <Card sx={{minWidth: 200, maxWidth: 200, minHeight: 200, maxHeight: 200,}}>
                            <CardActionArea component={item.url_name} to={item.url_path}>
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="div">
                                    {item.title}
                                </Typography>
                            </CardContent>
                            <CardMedia
                              component="img"
                              height="30%"
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