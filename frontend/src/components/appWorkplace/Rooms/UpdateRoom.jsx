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

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const UpdateRoom = () => {
    const roomParam = useParams()
    const roomId = roomParam.id
    const [room, setRooms] = useState()
    const [loading, setLoading] = useState(true)

    const GetData = async () => {
        await AxiosInstanse.get(`workplace/room/${roomId}/`).then((res) => {
            setRooms(res.data)
            setValue('name',res.data.name)
            setValue('floor',res.data.floor)
            setValue('building',res.data.building)
            setLoading(false)
        })
    }

    useEffect(() =>{
        GetData();
    },[])

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
        setValue,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

    const submission = useCallback((data) => {
        AxiosInstanse.put(`workplace/room/${roomId}/`,{
                name: data.name,
                floor: data.floor,
                building: data.building,
        })
        .then((res) => {
            navigate(`/room/list`)
        })
    })
    return(
        <div>
            {loading ? <LinearIndeterminate/> :
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Редактировать кабинет № {room.name}
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
                    <Box>
                        <ThemeProvider theme={darkTheme}>
                            <Box
                                display="flex"
                                justifyContent="space-between"
                                alignItems="center"
                            >
                                <Button variant='contained' type='submit'>Сохранить</Button>
                                <Button variant='contained' component={Link} to={`/room/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </form>}
        </div>

    )


}

export default UpdateRoom