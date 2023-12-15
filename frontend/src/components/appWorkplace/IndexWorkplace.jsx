import * as React from 'react';
import {createTheme, ThemeProvider} from "@mui/material/styles";
import {Card, CardActionArea, CardContent, CardMedia, Grid, Typography} from '@mui/material';
import {Link } from "react-router-dom";
import HomeWorkplace from "./Workplaces/HomeWorkplace";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const WorkplaceContent = [
    {'title': 'Рабочие места', 'url_path': '/workplace/list', 'url_name': HomeWorkplace, 'image': 'http://localhost/static/images/workplace.svg'},
    {'title': 'Помещение', 'url_path': '/workplace/room/list', 'url_name': 'HomeRoom', 'image': 'http://localhost/static/images/room.svg'},

];


const IndexWorkplace = () => {
    return (
        <Grid container style={{marginLeft: "50px"}}>
            <ThemeProvider theme={darkTheme}>
                {WorkplaceContent.map((item) => (
                    <Grid item xs={12} sm={6} md={4} style={{marginTop: "80px"}}>
                        <Card sx={{minWidth: 200, maxWidth: 200, minHeight: 200, maxHeight: 200,}}>
                            <CardActionArea component={Link} to={item.url_path} element={item.url_name}>
                                <CardContent>
                                    <Typography gutterBottom   component="div">
                                        {item.title}
                                    </Typography>
                                </CardContent>
                                <CardMedia
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

export default IndexWorkplace;