import * as React from 'react';
import {createTheme, ThemeProvider} from "@mui/material/styles";
import {Card, CardActionArea, CardContent, CardMedia, Grid, Typography} from '@mui/material';
import {Link } from "react-router-dom";
import ListOS from "./OS/ListOS";
import ListSofware from "./Software/ListSofware";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const SofwareContent = [
    {'title': 'ОС', 'url_path': '/software/list', 'url_name': ListSofware, 'image': 'http://localhost/static/images/software.svg'},
    {'title': 'ПО', 'url_path': '/os/list', 'url_name': ListOS, 'image': 'http://localhost/static/images/os.svg'},

];
export {SofwareContent}

const IndexSoftware = () => {
    return (
        <Grid container style={{marginLeft: "50px"}}>
            <ThemeProvider theme={darkTheme}>
                {SofwareContent.map((item) => (
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

export default IndexSoftware;