import * as React from 'react';
import TextField from '@mui/material/TextField';
import {Controller} from 'react-hook-form'

export default function CustomTextField(props) {
    const {label, width, placeholder, name, control, maxLength, type, id} = props
    return (
      
        <Controller
            name={name}
            control={control}
            maxLength={maxLength}
            render={({
                field:{onChange, value},
                fieldState: { error },
            }) => (
                <TextField
                    sx={{width:{width}}}
                    onChange={onChange}
                    value={value}
                    id={id}
                    label={label}
                    variant="standard"
                    type={type}
                    placeholder = {placeholder}
                    error = {!!error}
                    helperText = {error?.message}
                />
            )
            }
        />
  );
}