import {React, useCallback, useEffect, useState} from 'react'
import { Box, Button, Typography, Grid} from '@mui/material'
import CustomTextField from '../Forms/TextField';
import {useForm} from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import * as yup from 'yup'
import {createTheme} from '@mui/material/styles';
import AxiosInstanse from '../Axios';
import {useNavigate, Link} from 'react-router-dom';
import useCSRF from "../Hooks/CSRF";
import PrintError from "../Errors/Error";


const LoginApp = () => {
    const CSRF = useCSRF()
    const [error, setError] = useState();

    const defaultValues = {
            username: "",
            password: ""
    }

    const schema = yup
        .object({
            username: yup.string().required('Обязательное поле'),
            password: yup.string().required('Обязательное поле')
        }).required()

    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})


    const submission = useCallback((data) => {
        AxiosInstanse.post(`login/`,
            {
                username: data.username,
                password: data.password,
            },
            {
                headers: {
                    'X-CSRFToken': CSRF
                }
            }
        )
        .then((res) => {
            window.location.href=(`/`);
        })
        .catch((error) => {
            setError(error)
            console.log(error)
        })
    })
    return (
        <div>
            <Grid
                container
                spacing={2}
                direction="column"
                alignItems="center"
                justifyContent="center"
                sx={{ minHeight: '100vh' }}
            >
                <Grid item sx={3}>
                    <form onSubmit={handleSubmit(submission)}>
                        <Box sx={{display:'flex', width:'460px', borderRadius: 2, boxShadow:3, padding:4, flexDirection:'column'}}>
                            <Box sx={{display:'flex', justifyContent:'center',width:'100%',  marginBottom:'10px'}}>
                                <Typography>
                                    Авторизация
                                </Typography>
                            </Box>
                            <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                                <CustomTextField
                                    label='Имя пользователя'
                                    placeholder='Введите имя пользователя'
                                    name='username'
                                    control={control}
                                    width={'100%'}
                                    maxLength='15'
                                />
                            </Box>
                            <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                                <CustomTextField
                                    label='Пароль'
                                    placeholder='Введите пароль'
                                    name='password'
                                    type="password"
                                    control={control}
                                    width={'100%'}
                                    maxLength='25'
                                />
                            </Box>
                            {!error ? <></> :
                                <Box sx={{display:'flex',justifyContent:'space-around', marginBottom:'40px'}}>
                                    <PrintError error={error.message}/>
                                </Box>
                            }
                            <Box sx={{display:'flex',justifyContent:'space-around', marginBottom:'40px'}}>
                                <Button variant='contained' type='submit' color='inherit'>Войти</Button>
                            </Box>
                        </Box>
                    </form>
                </Grid>
            </Grid>
        </div>

    )
}

export default LoginApp;