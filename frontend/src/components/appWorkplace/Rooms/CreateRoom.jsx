import {React} from 'react'
import { Box, Button, Typography, Grid } from '@mui/material'
import CustomTextField from "../../Forms/TextField";
import {useForm} from 'react-hook-form'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate} from "react-router-dom";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const CreateRoom = () => {
    const navigate = useNavigate()
    const defaultValues = {
        name: '',
        floor: '',
        building: ''
    }
    const {
        handleSubmit,
        reset,
        setValue,
        control,
    } = useForm({defaultValues:defaultValues})
    const submission = (data) => {
        AxiosInstanse.post(`workplace/api/v1/room/`,{
                name: data.name,
                floor: data.floor,
                building: data.building,
        })
        .then((res) => {
            navigate(`/room/list`)
        })
    }
    return(
        <div>
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'space-between',width:'100%',  marginBottom:'10px'}}>
                    <Typography sx={{marginLeft:'20px',}}>
                        Create records
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                    <Grid item xs={12} sm={6} md={4} style={{marginBottom: "80px"}}>
                        <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                            <CustomTextField
                                label='Кабинет'
                                placeholder='Введите № кабинета'
                                name='name'
                                control={control}
                                width={'30%'}
                            />
                            <CustomTextField
                                label='Этаж'
                                placeholder='Введите № этажа'
                                name='floor'
                                control={control}
                                width={'30%'}
                            />
                            <CustomTextField
                                label='Здание'
                                placeholder='Введите название здания'
                                name='building'
                                control={control}
                                width={'30%'}
                            />
                        </Box>
                            <ThemeProvider theme={darkTheme}>
                                <Box>
                                    <Button variant='contained' type='submit' sx={{flexGrow:'1'}}>Сохранить</Button>
                                    <Button variant='contained'>Отмена</Button>
                                </Box>
                            </ThemeProvider>

                    </Grid>
                </Box>
            </form>
        </div>

    )


}

export default CreateRoom
