import * as React from 'react'
import TextField from '@mui/material/TextField'
import { Controller } from 'react-hook-form'
import PropTypes from 'prop-types'

export default function CustomTextField(props) {
  const { label, width, placeholder, name, control, maxLength, type, id } = props
  return (
    <Controller
      name={name}
      control={control}
      maxLength={maxLength}
      render={({ field: { onChange, value }, fieldState: { error } }) => (
        <TextField
          sx={{ width: { width } }}
          onChange={onChange}
          value={value}
          id={id}
          label={label}
          variant='standard'
          type={type}
          placeholder={placeholder}
          error={!!error}
          helperText={error?.message}
        />
      )}
    />
  )
}

CustomTextField.propTypes = {
  label: PropTypes.string,
  width: PropTypes.string,
  placeholder: PropTypes.string,
  name: PropTypes.string,
  control: PropTypes.object,
  maxLength: PropTypes.string,
  type: PropTypes.string,
  id: PropTypes.string,
}
