import {React} from 'react'
import { Box, Button, Typography} from '@mui/material'
import CustomTextField from "../../Forms/TextField";
import {useForm} from 'react-hook-form'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate} from "react-router-dom";
import {Container} from "reactstrap";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const CreateWorkplace = () => {
    const navigate = useNavigate()
    const defaultValues = {
        name: '',
        room: '',
    }
    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues})

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
            </form>
        </div>

    )


}

export default CreateWorkplace
