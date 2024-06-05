import * as React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import {Controller} from 'react-hook-form'
import FormHelperText from '@mui/material/FormHelperText';
import LinearIndeterminate from "../appHome/ProgressBar.jsx";
import PrintError from "../Errors/Error.jsx";
import PropTypes from "prop-types";

export default function SelectField(props) {
  
    const {label, name, control, width, options, loading, error} = props

    return (
        <>
            {loading ? <LinearIndeterminate width={width}/> :
                error ? <PrintError error={error} width={width}/> :
                    <Controller
                        name = {name}
                        control = {control}
                        render= {({
                            field:{onChange, value},
                            fieldState:{error},
                        }) => (
                            <FormControl variant="standard" sx={{ width:{width}}}>
                                <InputLabel id="demo-simple-select-filled-label">{label}</InputLabel>
                                <Select
                                    labelId="demo-simple-select-filled-label"
                                    id="demo-simple-select-filled"
                                    onChange={onChange}
                                    value={value}
                                    error = {!!error}
                                >
                                    {
                                        options.map((option, index) =>(
                                            <MenuItem key={index} value={option.id}>{option.name} </MenuItem>
                                        ))
                                    }
                                </Select>
                                <FormHelperText sx={{color:"#d32f2f"}}> {error.name ? true : false} </FormHelperText>
                            </FormControl>
                        )}
                    />

            }
    </>
  );
};

SelectField.propTypes = {
    options: PropTypes.node, 
    loading: PropTypes.bool,
    error: PropTypes.node,
    label: PropTypes.string, 
    width: PropTypes.string, 
    placeholder: PropTypes.string, 
    name: PropTypes.string, 
    control: PropTypes.node, 
    maxLength: PropTypes.number, 
    type: PropTypes.string, 
    id: PropTypes.string, 
}