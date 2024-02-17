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

const options = [

]

const CreatePost = () => {

    const [dep, setDeps] = useState()
    const [value, setValues] = useState(options.id)
    const [loading, setLoading] = useState(true)
    const navigate = useNavigate()

    const GetData = () => {
        AxiosInstanse.get(`employee/departament/`).then((res) => {
            setDeps(res.data)
            console.log(res.data)
            setLoading(false)
        })
    }

    useEffect(() =>{
        GetData();
    },[])

    const defaultValues = {
        name: '',
        departament: '',
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле'),
            departament: yup.string(),
        })
      .required()

    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

    const submission =useCallback( async (data) => {
        await AxiosInstanse.post(`employee/post/`,{
                name: data.name,
                departament: data.departament,
        })
        .then((res) => {
            navigate(`/post/list`)
        })
    })
    return(
        <div>
            {loading ? <LinearIndeterminate/> :
                <form onSubmit={handleSubmit(submission)}>
                    <Box sx={{display:'flex', justifyContent:'center',width:'100%',  marginBottom:'10px'}}>
                        <Typography>
                            Добавить должность
                        </Typography>
                    </Box>
                    <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                        <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                            <CustomTextField
                                label='Должность'
                                placeholder='Введите должность'
                                name='name'
                                control={control}
                                width={'30%'}
                                maxlength='50'
                            />
                            <AutocompleteField
                                name='departament'
                                control={control}
                                width={'30%'}
                                options={dep}
                                label='Выберите отдел'
                                placeholder='Выберите отдел'
                                noOptionsText='Отдел не обнаружен'
                                optionLabel={(option) => `${option.name}`}
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
                                    <Button variant='contained' component={Link} to={`/post/list`}>Отмена</Button>
                                </Box>
                            </ThemeProvider>
                        </Box>
                    </Box>
                </form>
            }
        </div>

    )


}

export default CreatePost
