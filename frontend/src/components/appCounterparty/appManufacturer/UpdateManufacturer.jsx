import {React, useEffect, useState, useCallback} from 'react'
import { Box, Button, Typography,} from '@mui/material'
import CustomTextField from "../../Forms/TextField";
import {useForm} from 'react-hook-form'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate,useParams,Link} from "react-router-dom";
import LinearIndeterminate from "../../appHome/ProgressBar";
import * as yup from "yup";
import {yupResolver} from "@hookform/resolvers/yup";
import PrintError from "../../Errors/Error.jsx";
import useCSRF from "../../Hooks/CSRF.jsx";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const UpdateManufacturer = () => {
    const CSRF = useCSRF()
    const mnfParam = useParams()
    const mnfId = mnfParam.id
    const [mnf, setMnfs] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [errorEdit, setErrorEdit] = useState(null)

    const GetData = async () => {
        try {
            await AxiosInstanse.get(`counterparty/manufacturer/${mnfId}/`).then((res) => {
                setMnfs(res.data)
                setValue('name',res.data.name)
                setValue('country',res.data.country)
                setValue('production',res.data.production)
            })
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false)
        }

    }

    useEffect(() =>{
        GetData();
    },[])

    const navigate = useNavigate()
    const defaultValues = {
        name: '',
        country: '',
        production: ''
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле').max(150, `Должно быть короче 150 символов`),
            country: yup.string().max(150, `Должно быть короче 150 символов`),
            production: yup.string().max(150, `Должно быть короче 150 символов`),
        })
      .required()

    const {
        handleSubmit,
        setValue,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

    const submission = useCallback((data) => {
        AxiosInstanse.put(`counterparty/manufacturer/${mnfId}/`,{
                name: data.name,
                country: data.country,
                production: data.production,
        },{
            headers: {
                    'X-CSRFToken': CSRF
                }
        })
        .then(() => {
            navigate(`/manufacturer/list`)
        }).catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    })
    return(
        <>
            {loading ? <LinearIndeterminate/> :
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Редактировать кабинет № {
                            loading ? <LinearIndeterminate/> :
                                error ? <PrintError error={error}/>
                                    :mnf.name
                        }
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Производитель'
                            placeholder='Введите название производителя'
                            name='name'
                            control={control}
                            width={'30%'}
                            maxLength='15'
                        />
                        <CustomTextField
                            label='Страна производителя'
                            placeholder='Введите название страны производителя'
                            name='country'
                            control={control}
                            width={'30%'}
                            maxLength='25'
                        />
                        <CustomTextField
                            label='Страна производства'
                            placeholder='Введите название страны производства'
                            name='production'
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
                                <Button variant='contained' type='submit'>Сохранить</Button>
                                <Button variant='contained' component={Link} to={`/manufacturer/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </form>}
        </>

    )


}

export default UpdateManufacturer