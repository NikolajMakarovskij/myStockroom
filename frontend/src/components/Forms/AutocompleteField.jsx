import {React} from 'react';
import {TextField, FormControl, FormHelperText} from '@mui/material';
import {Controller} from 'react-hook-form';
import Autocomplete from '@mui/material/Autocomplete';
import LinearIndeterminate from "../appHome/ProgressBar.jsx";
import PrintError from "../Errors/Error.jsx";

export default function AutocompleteField(props) {

    const {label, optionLabel, name, id, control, placeholder, width, options, noOptionsText, loading, error} = props;

    return (
        <>
            {loading ? <LinearIndeterminate width={width}/> :
                error ? <PrintError error={error} width={width}/> :
                    <Controller
                        name={name}
                        control={control}
                        render={({
                            field: {onChange, value, name},
                            fieldState: {error},
                        }) => (
                            <FormControl variant="standard" sx={{width: {width}}}>
                                <Autocomplete
                                    name={name}
                                    value={value ? options.find((option) => {
                                        return value === option.id
                                    }) ?? null : null}
                                    options={options}
                                    getOptionLabel={optionLabel}
                                    isOptionEqualToValue={(option, value) => option.id === value}
                                    noOptionsText={noOptionsText}
                                    id={id}
                                    disableCloseOnSelect
                                    renderInput={(params) => (
                                        <TextField {...params} label={label} placeholder={placeholder} value={value}
                                                   variant="standard"/>
                                    )}
                                    onChange={(event, newValues) => {
                                        onChange(newValues ? newValues.id : null)
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