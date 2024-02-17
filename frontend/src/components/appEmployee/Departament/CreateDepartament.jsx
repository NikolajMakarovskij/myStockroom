import {React, useCallback} from 'react'
import { Box, Button, Typography} from '@mui/material'
import CustomTextField from '../../Forms/TextField';
import {useForm} from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import * as yup from 'yup'
import {createTheme, ThemeProvider} from '@mui/material/styles';
import AxiosInstanse from '../../Axios';
import {useNavigate, Link} from 'react-router-dom';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const CreateDepartament = () => {
    const navigate = useNavigate()
    const defaultValues = {
        name: '',
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле'),
        })
      .required()

    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

    const submission = useCallback(async (data) => {
        await AxiosInstanse.post(`employee/departament/`,{
                name: data.name,
        })
        .then((res) => {
            navigate(`/departament/list`)
        })
    })
    return(
        <div>
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center',width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Добавить отдел
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Отдел'
                            placeholder='Введите название отдела'
                            name='name'
                            control={control}
                            width={'100%'}
                            maxLength='50'
                        />
                    </Box>
                    <Box>
                        <ThemeProvider theme={darkTheme}>
                            <Box
                                display="flex"
                                justifyContent="space-between"
                                alignItems="center"
                            >
                                <Button variant='contained' type='submit' >Сохранить</Button>
                                <Button variant='contained' component={Link} to={`/departament/list`} >Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>

                </Box>
            </form>
        </div>

    )


}

export default CreateDepartament
