import {React} from 'react'
import {Typography, Alert, AlertTitle} from '@mui/material';

export default function PrintError({error, width}) {
    return(
        <Alert
            sx={{width: {width}}}
            elevation={24}
            variant="filled"
            severity="error"
        >
            <Typography
                variant="h5"
            >
                <AlertTitle>Error</AlertTitle>
                {error}
            </Typography>

        </Alert>
    )
}