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
import AutocompleteField from "../../Forms/AutocompleteField";
import useInterval from "../../Hooks/useInterval";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const UpdatePost = () => {
    const postParam = useParams()
    const postId = postParam.id
    const [dep, setDeps  ] = useState()
    const [post, setPosts ] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [delay, setDelay] = useState(100)

    useInterval(() => {

        async function getData() {
            try {
                await AxiosInstanse.get(`employee/post/${postId}/`).then((res) => {
                    setPosts(res.data)
                    setValue('name',res.data.name)
                    setValue('departament',res.data.departament)
                })
                await AxiosInstanse.get(`employee/departament/`).then((res) => {
                    setDeps(res.data)
                    setLoading(false)
                    setError(null)
                    setDelay(5000)
                })
                } catch (error) {
                    setError(error.message);
                    setDelay(null)
                } finally {
                    setLoading(false);
                }
        }
        getData();
    }, delay);

    const navigate = useNavigate()
    const defaultValues = {
        name: '',
        departament: '',
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
        AxiosInstanse.put(`employee/post/${postId}/`,{
                name: data.name,
                departament: data.departament,
        })
        .then((res) => {
            navigate(`/post/list`)
        })
    }
    return(
        <div>
            {loading ? <LinearIndeterminate/> :
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Редактировать должность {post.name}
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
                        />
                        <AutocompleteField
                            loading={loading}
                            error={error}
                            name='departament'
                            control={control}
                            width={'30%'}
                            options={dep}
                            label='Выберите отдел'
                            placeholder='Выберите отдел'
                            noOptionsText='Отделы не обнаружены'
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
            </form>}
        </div>

    )


}

export default UpdatePost