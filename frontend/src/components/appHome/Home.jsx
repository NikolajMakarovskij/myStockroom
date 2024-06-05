import * as React from 'react';
import {createTheme, ThemeProvider} from "@mui/material/styles";
import {Card, CardActionArea, CardContent, CardMedia, Grid, Typography} from '@mui/material';
import {Link } from "react-router-dom";

import IndexWorkplace from "../appWorkplace/IndexWorkplace";
import IndexDevice from "../appDevice/IndexDevice";
import IndexStock from "../appStock/IndexStock";
import IndexCounterparty from "../appCounterparty/IndexCounterparty";
import IndexAccounting from "../appAccounting/IndexAccounting";
import IndexSignature from "../appSignature/IndexSignature.jsx";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const HomeContent = [
    {key: 'stock', 'title': "Склад", 'url_path': '/stock', 'url_name': IndexStock, 'image': 'http://localhost/static/images/warehouse.svg'},
    {key: 'consumables', 'title': "Расходники", 'url_path': '/consumables', 'url_name': 'core:index', 'image': 'http://localhost/static/images/consumables.svg'},
    {key: 'counterparty', 'title': "Контрагенты", 'url_path': '/counterparty', 'url_name': IndexCounterparty, 'image': 'http://localhost/static/images/post.svg'},
    {key: 'workplace', 'title': "Рабочие места", 'url_path': '/workplace', 'url_name': IndexWorkplace, 'image': 'http://localhost/static/images/workplace.svg'},
    {key: 'device', 'title': "Устройства", 'url_path': '/device', 'url_name': IndexDevice, 'image': 'http://localhost/static/images/device.svg'},
    {key: 'software', 'title': "Софт", 'url_path': '/software', 'url_name': 'core:index', 'image': 'http://localhost/static/images/software.svg'},
    {key: 'signature', 'title': "ЭЦП", 'url_path': '/signature', 'url_name': IndexSignature, 'image': 'http://localhost/static/images/signature.svg'},
    {key: 'employee', 'title': "Сотрудники", 'url_path': '/employee', 'url_name': 'core:index', 'image': 'http://localhost/static/images/employee.svg'},
    {key: 'accounting', 'title': "Баланс", 'url_path': '/accounting', 'url_name': IndexAccounting, 'image': 'http://localhost/static/images/accounting.svg'},
];


const Home = () => {
    return (
        <Grid container style={{marginLeft: "50px"}}>
            <ThemeProvider theme={darkTheme}>
                {HomeContent.map((item) => (
                    <Grid key={item.key} item xs={12} sm={6} md={4} style={{marginBottom: "80px"}}>
                        <Card sx={{minWidth: 200, maxWidth: 200, minHeight: 200, maxHeight: 200, borderRadius: 5,
                        display: 'flex'}}>
                            <CardActionArea component={Link} to={item.url_path} element={item.url_name}
                                            sx={{ display: 'flex', flexDirection: 'column' }}>
                                <CardContent>
                                    <Typography gutterBottom component="div">
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

export default Home;