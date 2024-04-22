import {React, useState} from 'react';
import {TextField, FormControl, FormHelperText} from '@mui/material';
import {Controller} from 'react-hook-form';
import Autocomplete from '@mui/material/Autocomplete';
import LinearIndeterminate from "../appHome/ProgressBar.jsx";
import PrintError from "../Errors/Error.jsx";

export default function AutocompleteMultipleField(props) {

    const {label, optionLabel, name, id, control, placeholder, width, options, noOptionsText, loading, error} = props;
    const [value, setValues] = useState([]);
    const handleChange = (event) => {
        setValues(event.target.value);
    };

    return (
        <>
            {loading ? <LinearIndeterminate width={width}/> :
                error ? <PrintError error={error} width={width}/> :
                    <Controller
                        name={name}
                        control={control}
                        render={({
                            field: {onChange, value, name, ref},
                            fieldState: {error},
                            formState,
                        }) => (
                            <FormControl variant="standard" sx={{width: {width}}}>
                                <Autocomplete
                                    multiple
                                    filterSelectedOptions
                                    id={id}
                                    name={name}
                                    options={options}
                                    getOptionLabel={optionLabel}
                                    // не получается осилить возврат массива из id, по умолчанию value задан как []
                                    /*value={value ? options.find((option) => {
                                        return value === option.id // не возвращает массив
                                    }) ?? [] : []}*/
                                    value={value ? value : []} // возвращает весь массив объектов
                                    isOptionEqualToValue={(option, value) => option.id === value.id}
                                    noOptionsText={noOptionsText}
                                    disableCloseOnSelect
                                    renderInput={(params) => (
                                        <TextField
                                            {...params}
                                            label={label}
                                            placeholder={placeholder}
                                            inputRef={ref}
                                            value={value}
                                            variant="standard"/>
                                    )}
                                    onChange={(event, newValue) => {
                                        onChange(newValue ?
                                         newValue : [])


                                    }}
                                />
                                <FormHelperText sx={{color: "#d32f2f"}}> {error?.message} </FormHelperText>
                                </FormControl>
                            )}
                        />
            }
        </>
    );
}