import { React } from 'react'
import PropTypes from 'prop-types'
import { Typography, Alert, AlertTitle } from '@mui/material'

export default function PrintError({ error, width }) {
  return (
    <Alert sx={{ width: { width } }} elevation={24} variant='filled' severity='error'>
      <Typography variant='h5'>
        <AlertTitle>Error</AlertTitle>
        {error}
      </Typography>
    </Alert>
  )
}

PrintError.propTypes = {
  width: PropTypes.string,
  error: PropTypes.node,
}
