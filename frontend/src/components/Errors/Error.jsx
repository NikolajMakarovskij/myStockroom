import {React, useState} from 'react'
import {Typography, Alert, AlertTitle, Paper, styled} from '@mui/material';

export default function PrintError({error}) {
    const [value, setValue] = useState(error)
    return(
        <Alert
            elevation={24}
            variant="filled"
            severity="error"
        >
            <Typography
                variant="h5"
            >
                <AlertTitle>Error</AlertTitle>
                {value}
            </Typography>

        </Alert>
    )
}