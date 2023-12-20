import {React, useEffect, useState} from 'react'
import { Box, Button, Typography,} from '@mui/material'
import CustomTextField from "../../Forms/TextField";
import {useForm} from 'react-hook-form'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate,useParams} from "react-router-dom";
import {Container} from "reactstrap";
import LinearIndeterminate from "../../appHome/ProgressBar";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const UpdateWorkplace = () => {
    const workplaceParam = useParams()
    const workplaceId = workplaceParam.id
    const [workplace, setWorkplaces] = useState()
    const [loading, setLoading] = useState(true)

    const GetData = () => {
        AxiosInstanse.get(`workplace/api/v1/workplace/${workplaceId}/`).then((res) => {
            setWorkplaces(res.data)
            setValue('name',res.data.name)
            setValue('room',res.data.room.name)
            setLoading(false)
        })
    }

    useEffect(() =>{
        GetData();
    },)

    const navigate = useNavigate()
    const defaultValues = {
        name: '',
        room: '',
    }


    const {
        handleSubmit,
        setValue,
        control,
    } = useForm({defaultValues:defaultValues})
    const submission = (data) => {
        AxiosInstanse.put(`workplace/api/v1/workplace/${workplaceId}/`,{
                name: data.name,
                room: data.room.id,
        })
        .then((res) => {
            navigate(`/workplace/list`)
        })
    }
    return(
        <div>
            {loading ? <LinearIndeterminate/> :
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Редактировать кабинет № {workplace.name}
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
                        <CustomTextField
                            label='Кабинет'
                            placeholder='Укажите № кабинета'
                            name='room'
                            control={control}
                            width={'30%'}
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
            </form>}
        </div>

    )


}

export default UpdateWorkplace