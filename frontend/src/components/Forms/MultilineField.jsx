import * as React from 'react';
import TextField from '@mui/material/TextField';
import {Controller} from 'react-hook-form'

export default function MultilineField(props) {
    const {label, placeholder, width,name, control, rows, id} = props
    return (
        <Controller
            name = {name}
            control = {control}
            render= {({
                field:{onChange, value},
                fieldState:{error},
            }) => (
                <TextField
                    id={id}
                    sx={{width:{width}}}
                    label={label}
                    multiline
                    onChange={onChange}
                    value={value}
                    rows={rows}
                    variant="standard"
                    placeholder = {placeholder}
                    error = {!!error}
                    helperText = {error?.message}
                />
            )}
        />
    );
  }
