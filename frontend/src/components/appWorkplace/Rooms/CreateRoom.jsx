import {React, useCallback, useState} from 'react'
import { Box, Button, Typography} from '@mui/material'
import CustomTextField from '../../Forms/TextField';
import {useForm, Form} from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import * as yup from 'yup'
import {createTheme, ThemeProvider} from '@mui/material/styles';
import AxiosInstanse from '../../Axios';
import {useNavigate, Link} from 'react-router-dom';
import PrintError from "../../Errors/Error";
import useCSRF from "../../Hooks/CSRF";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const CreateRoom = () => {
    const CSRF = useCSRF()
    const [errorEdit, setErrorEdit] = useState(null)
    const navigate = useNavigate()
    const defaultValues = {
        name: '',
        floor: '',
        building: ''
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле').max(15, `Должно быть короче 15 символов`),
            floor: yup.string().max(25, `Должно быть короче 25 символов`),
            building: yup.string().max(25, `Должно быть короче 25 символов`),
        })
      .required()

    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

    const submission = useCallback((data) => {
        AxiosInstanse.post(`workplace/room/`,{
                name: data.name,
                floor: data.floor,
                building: data.building,
        },{
            headers: {
                    'X-CSRFToken': CSRF
                }
        })
        .then((res) => {
            navigate(`/room/list`)
        })
        .catch((error) => {
            setErrorEdit(error.response.data.detail)
        });

    })
    return(
        <div>
            <form
                onSubmit={handleSubmit(submission)}
            >
                <Box sx={{display:'flex', justifyContent:'center',width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Добавить кабинет
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Кабинет'
                            placeholder='Введите № кабинета'
                            name='name'
                            control={control}
                            width={'30%'}
                            maxLength='15'
                        />
                        <CustomTextField
                            label='Этаж'
                            placeholder='Введите № этажа'
                            name='floor'
                            control={control}
                            width={'30%'}
                            maxLength='25'
                        />
                        <CustomTextField
                            label='Здание'
                            placeholder='Введите название здания'
                            name='building'
                            control={control}
                            width={'30%'}
                            maxLength='25'
                        />
                    </Box>
                    {!errorEdit ? <></> :
                        <Box sx={{display:'flex',justifyContent:'space-around', marginBottom:'40px'}}>
                            <PrintError error={errorEdit}/>
                        </Box>
                    }
                    <Box>
                        <ThemeProvider theme={darkTheme}>
                            <Box
                                display="flex"
                                justifyContent="space-between"
                                alignItems="center"
                            >
                                <Button variant='contained' type='submit' >Сохранить</Button>
                                <Button variant='contained' component={Link} to={`/room/list`} >Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>

                </Box>
            </form>
        </div>

    )


}

export default CreateRoom
