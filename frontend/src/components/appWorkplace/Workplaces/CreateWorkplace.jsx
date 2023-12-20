import {React, useState, useEffect} from 'react'
import { Box, Button, Typography} from '@mui/material'
import CustomTextField from "../../Forms/TextField";
import {useForm} from 'react-hook-form'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate} from "react-router-dom";
import {Container} from "reactstrap";
import LinearIndeterminate from "../../appHome/ProgressBar";
import SelectField from "../../Forms/SelectField";
import * as yup from "yup";
import {yupResolver} from "@hookform/resolvers/yup";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const CreateWorkplace = () => {

    const [room, setRooms] = useState()
    const [loading, setLoading] = useState(true)
    const navigate = useNavigate()

    const GetData = () => {
        AxiosInstanse.get(`workplace/api/v1/room/`).then((res) => {
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
            name: yup.string().required('Обязательное поле'),
            room: yup.string(),
        })
      .required()

    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

    const submission = (data) => {
        AxiosInstanse.post(`workplace/api/v1/workplace/`,{
                name: data.name,
                room: data.room,
        })
        .then((res) => {
            navigate(`/workplace/list`)
        })
    }
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
                            <SelectField
                                label='Кабинет'
                                name='room'
                                control={control}
                                width={'30%'}
                                options={room}
                            />
                        </Box>
                        <Container>
                            <ThemeProvider theme={darkTheme}>
                                <Box
                                    display="flex"
                                    justifyContent="space-between"
                                    alignItems="center"
                                >
                                    <Button variant='contained' type='submit'>Сохранить</Button>
                                    <Button variant='contained'>Отмена</Button>
                                </Box>
                            </ThemeProvider>
                        </Container>
                    </Box>
                </form>
            }
        </div>

    )


}

export default CreateWorkplace
