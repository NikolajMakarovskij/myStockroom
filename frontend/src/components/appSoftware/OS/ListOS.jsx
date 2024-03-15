import {React} from 'react'
import {Typography, Paper, Grid, Alert, AlertTitle} from '@mui/material';

const ListOS = () => {
    return (
        <Grid
            container
            direction="column"
            alignItems="center"
            justifyContent="center" sx={{minHeight: '100vh'}}
        >
            <Grid>
                <Alert
                    elevation={24}
                    variant="filled"
                    severity="info"
                >
                    <AlertTitle>info</AlertTitle>
                    <Typography variant="h1">
                        Раздел в разработке
                    </Typography>
                </Alert>
            </Grid>
        </Grid>
    )
}

export default ListOS;