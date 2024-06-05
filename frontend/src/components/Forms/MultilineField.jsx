import * as React from 'react';
import TextField from '@mui/material/TextField';
import {Controller} from 'react-hook-form'
import PropTypes from "prop-types";

export default function MultilineField(props) {
    const {label, placeholder, width, name, control, rows, id} = props
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

MultilineField.propTypes = {
    label: PropTypes.string, 
    placeholder: PropTypes.string, 
    width: PropTypes.string,
    name: PropTypes.string,
    control: PropTypes.object,
    rows: PropTypes.number,
    id: PropTypes.string,
}  