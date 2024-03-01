import {React, useCallback, useEffect, useState} from 'react'
import { Box, Button, Typography} from '@mui/material'
import CustomTextField from '../Forms/TextField';
import {useForm, Form} from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import * as yup from 'yup'
import {createTheme, ThemeProvider} from '@mui/material/styles';
import AxiosInstanse from '../Axios';
import {useNavigate, Link} from 'react-router-dom';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const LoginApp = () => {
    const [csrf, setCsrf] = useState();
    const [username, setUsername] = useState();
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const navigate = useNavigate()

    const GetCSRF = useCallback(async () => {
        await AxiosInstanse.get(`csrf/`,  {credentials: 'include'})
            .then((res) => {
                let csrfToken = res.headers.get("X-CSRFToken")
                setCsrf(csrfToken)
            })
            .catch((e) => {
                console.log(e)
            })

    })

    const GetSession = useCallback(async () => {
        await AxiosInstanse.get(`session/`,  {credentials: 'include'}).then((res) => {
            if (!res.data.isAuthenticated) {
                setIsAuthenticated(true)
                GetCSRF()
            } else {
                setIsAuthenticated(res.data.isAuthenticated)
                setUsername(res.data.username)
            }
        })

    })

    useEffect(() =>{
        GetSession();
    },[])

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
        AxiosInstanse.post(`login/`,{body: JSON.stringify({
                username: data.username,
                password: data.password,
        })},
        {withCredentials: true},
        {credentials: 'include'},
        {headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf,
        }}
        )
        .then((res) => {
            navigate(`login/`)
        })
            .catch((error) => {
              console.log(error)
            })
    })
    return (
<div>
            <form
                onSubmit={handleSubmit(submission)}
            >
                <Box sx={{display:'flex', justifyContent:'center',width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Авторизация
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Имя пользователя'
                            placeholder='Введите имя пользователя'
                            name='username'
                            control={control}
                            width={'30%'}
                            maxLength='15'
                        />
                        <CustomTextField
                            label='Пароль'
                            placeholder='Введите пароль'
                            name='password'
                            type="password"
                            control={control}
                            width={'30%'}
                            maxLength='25'
                        />
                    </Box>
                    <Box>
                        <ThemeProvider theme={darkTheme}>
                            <Box
                                display="flex"
                                justifyContent="space-between"
                                alignItems="center"
                            >
                                <Button variant='contained' type='submit' >Войти</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>

                </Box>
            </form>
        </div>

    )
}

export default LoginApp;