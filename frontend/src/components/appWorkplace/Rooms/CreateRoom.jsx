import {React} from 'react'
import { Box, Button, Typography} from '@mui/material'
import CustomTextField from '../../Forms/TextField';
import {useForm} from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import * as yup from 'yup'
import {createTheme, ThemeProvider} from '@mui/material/styles';
import AxiosInstanse from '../../Axios';
import {useNavigate} from 'react-router-dom';
import {Container} from 'reactstrap';

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

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле'),
            floor: yup.string(),
            building: yup.string(),
        })
      .required()

    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

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
                <Box sx={{display:'flex', justifyContent:'center',width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Добавить кабинет
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
                    <Container>
                        <ThemeProvider theme={darkTheme}>
                            <Box
                                display="flex"
                                justifyContent="space-between"
                                alignItems="center"
                            >
                                <Button variant='contained' type='submit' >Сохранить</Button>
                                <Button variant='contained' >Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Container>

                </Box>
            </form>
        </div>

    )


}

export default CreateRoom
