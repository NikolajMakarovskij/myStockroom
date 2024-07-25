import { React } from 'react'
import { TextField, FormControl, FormHelperText } from '@mui/material'
import { Controller } from 'react-hook-form'
import Autocomplete from '@mui/material/Autocomplete'
import LinearIndeterminate from '../appHome/ProgressBar.jsx'
import PrintError from '../Errors/Error.jsx'
import PropTypes from 'prop-types'

export default function AutocompleteMultipleField(props) {
  const { label, optionLabel, name, id, control, placeholder, width, options, noOptionsText, loading, error } = props

  //const selectedValue = useMemo(value ? (() => options.filter((option) => option.id), [options]) ?? [] : [])

  return (
    <>
      {loading ? (
        <LinearIndeterminate width={width} />
      ) : error ? (
        <PrintError error={error} width={width} />
      ) : (
        <Controller
          name={name}
          control={control}
          render={({ field: { onChange, value, name, ref }, fieldState: { error } }) => (
            <FormControl variant='standard' sx={{ width: { width } }}>
              <Autocomplete
                multiple
                //filterSelectedOptions
                id={id}
                name={name}
                options={options}
                getOptionLabel={optionLabel}
                value={
                  value
                    ? options.filter((item) => {
                        return value === item.id
                      }) ?? []
                    : []
                }
                //value={value ? value : []} // возвращает весь массив объектов
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
                    variant='standard'
                  />
                )}
                onChange={(event, newValue) => {
                  onChange(newValue ? newValue.id : [])
                }}
              />
              {console.log(value)}
              <FormHelperText sx={{ color: '#d32f2f' }}> {error?.message} </FormHelperText>
            </FormControl>
          )}
        />
      )}
    </>
  )
}

AutocompleteMultipleField.propTypes = {
  label: PropTypes.string,
  optionLabel: PropTypes.func,
  name: PropTypes.string,
  id: PropTypes.string,
  control: PropTypes.object,
  placeholder: PropTypes.string,
  width: PropTypes.string,
  options: PropTypes.array,
  noOptionsText: PropTypes.node,
  loading: PropTypes.bool,
  error: PropTypes.node,
}
