import {React, useState, useEffect, useCallback} from 'react'
import { Box, Button, Typography, TextField} from '@mui/material'
import CustomTextField from "../../Forms/TextField";
import {useForm} from 'react-hook-form'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate, Link} from "react-router-dom";
import LinearIndeterminate from "../../appHome/ProgressBar";
import * as yup from "yup";
import {yupResolver} from "@hookform/resolvers/yup";
import AutocompleteField from "../../Forms/AutocompleteField";
import Modal from "../../Modal/Modal.jsx";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const options = []

const CreateWorkplace = () => {

    const [room, setRooms] = useState()
    const [value, setValues] = useState(options.id)
    const [loading, setLoading] = useState(true)
    const navigate = useNavigate()

    const GetData = async () => {
        await AxiosInstanse.get(`workplace/room/`).then((res) => {
            setRooms(res.data)
            console.log(res.data)
            setLoading(false)
        })
    }

    useEffect(() =>{
        GetData();
    },[])

    const defaultValues = {
        name: '',
        room: '',
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле').max(50, 'Должно быть короче 50 символов'),
        })
      .required()

    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

    const submission =useCallback( (data) => {
        AxiosInstanse.post(`workplace/workplace/`,{
                name: data.name,
                room: data.room,
        })
        .then((res) => {
            navigate(`/workplace/list`)
        })
    })
    return(
        <div>
            {loading ? <LinearIndeterminate/> :
                <form onSubmit={handleSubmit(submission)}>
                    <Box sx={{display:'flex', justifyContent:'center',width:'100%',  marginBottom:'10px'}}>
                        <Typography>
                            Добавить рабочее место
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
                                maxlength='50'
                            />
                            <AutocompleteField
                                name='room'
                                control={control}
                                width={'30%'}
                                options={room}
                                label='Выберите кабинет'
                                placeholder='Выберите № кабинета'
                                noOptionsText='Кабинеты не обнаружены'
                                optionLabel={(option) => `${option.name} (здание: ${option.building}, этаж: ${option.floor})`}
                            />
                        </Box>
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
            }
        </div>

    )


}

export default CreateWorkplace
