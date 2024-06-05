import {React, useEffect, useState} from 'react'
import { Box, Button, Typography,} from '@mui/material'
import CustomTextField from "../../Forms/TextField";
import {useForm} from 'react-hook-form'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate,useParams,Link} from "react-router-dom";
import LinearIndeterminate from "../../appHome/ProgressBar";
import * as yup from "yup";
import {yupResolver} from "@hookform/resolvers/yup";
import AutocompleteField from "../../Forms/AutocompleteField.jsx";
import useInterval from "../../Hooks/useInterval"
import PrintError from "../../Errors/Error";
import useCSRF from "../../Hooks/CSRF";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const UpdateWorkplace = () => {
    const CSRF = useCSRF()
    const workplaceParam = useParams()
    const workplaceId = workplaceParam.id
    const [rooms, setRooms  ] = useState()
    const [workplace, setWorkplaces ] = useState()
    const [loading, setLoading] = useState(true)
    const [loadingData, setLoadingData] = useState(true)
    const [errorData, setErrorData] = useState(null)
    const [errorEdit, setErrorEdit] = useState(null)
    const [error, setError] = useState(null)
    const [delay, setDelay] = useState(100)

    useInterval(() => {

        async function getData() {
            try {
                await AxiosInstanse.get(`workplace/room/`).then((res) => {
                    setRooms(res.data)
                    setErrorData(null)
                    setDelay(5000)
                })
            } catch (error) {
                setErrorData(error.message);
                setDelay(null)

            } finally {
                setLoadingData(false)
            }
        }
        getData();
    }, delay);

    async function getCurrentData() {
        try {
                await AxiosInstanse.get(`workplace/workplace/${workplaceId}/`).then((res) => {
                    setWorkplaces(res.data)
                    setValue('name',res.data.name)
                    setValue('room',res.data.room)
                })
        } catch (error) {
            setError(error.message);
            setDelay(null)
        } finally {
            setLoading(false)
        }
    }
    useEffect(() => {
        getCurrentData()
    }, []);


    const navigate = useNavigate()
    const defaultValues = {
        name: '',
        room: '',
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле').max(50, 'Должно быть короче 50 символов')
        })
      .required()

    const {
        handleSubmit,
        setValue,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})
    const submission = (data) => {
        AxiosInstanse.put(`workplace/workplace/${workplaceId}/`,{
                name: data.name,
                room: data.room,
        },{
            headers: {
                    'X-CSRFToken': CSRF
                }
        })
        .then(() => {
            navigate(`/workplace/list`)
        }).catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    }

    return(
        <>
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Редактировать кабинет № {
                            loading ? <LinearIndeterminate/> :
                                error ? <PrintError error={error}/>
                                    :workplace.name
                        }
                        </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Рабочее место'
                            placeholder='Введите № рабочего места'
                            name='name'
                            control={control}
                            width={'30%'}
                        />
                        <AutocompleteField
                            loading={loadingData}
                            error={errorData}
                            name='room'
                            control={control}
                            width={'30%'}
                            options={rooms}
                            label='Выберите кабинет'
                            placeholder='Выберите № кабинета'
                            noOptionsText='Кабинеты не обнаружены'
                            optionLabel={(option) => `${option.name} (здание: ${option.building}, этаж: ${option.floor})`}
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
                                <Button variant='contained' component={Link} to={`/workplace/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </form>
        </>

    )


}

export default UpdateWorkplace