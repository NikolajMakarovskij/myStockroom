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
import useCSRF from "../../Hooks/CSRF.jsx";
import PrintError from "../../Errors/Error.jsx";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const UpdateAccessoriesCategory = () => {
    const CSRF = useCSRF()
    const catParam = useParams()
    const catId = catParam.id
    const [category, setCategory] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [errorEdit, setErrorEdit] = useState(null)

    async function getCurrentData() {
        try {
            await AxiosInstanse.get(`consumables/accessories_category/${catId}/`).then((res) => {
                    setCategory(res.data)
                    setValue('name',res.data.name)
                    setValue('slug',res.data.slug)
            })
        } catch (error) {
            setError(error.message);
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
        slug: '',
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле').max(50, 'Должно быть короче 50 символов'),
            slug: yup.string().required('Обязательное поле')
                .min(3, 'Must have at least 3 characters.')
                .max(16, 'Cannot be longer than 16 characteres.')
                .lowercase()
                .trim()
                .matches(/^(?![0-9-]+$)(?:[a-z]{2,}-?|[0-9]-?)+(?<!-)$/gm,
                    'Должно начинаться с буквы и может содержать только буквы, цифры или тире (не более одного подряд).')
        })
      .required()

    const {
        handleSubmit,
        setValue,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})
    const submission = (data) => {
        AxiosInstanse.put(`consumables/accessories_category/${catId}/`,{
                name: data.name,
                slug: data.slug,
        },{
            headers: {
                    'X-CSRFToken': CSRF
                }
        })
        .then(() => {
            navigate(`/accessories/categories/list`)
        })
        .catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    }
    return(
        <>
            {loading ? <LinearIndeterminate/> :
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Редактировать группу {
                            loading ? <LinearIndeterminate/> :
                                error ? <PrintError error={error}/>
                                    :category.name
                        }
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Группа'
                            placeholder='Введите название группы'
                            name='name'
                            control={control}
                            width={'30%'}
                            maxlength='50'
                        />
                        <CustomTextField
                            label='Ссылка'
                            placeholder='Введите ссылку'
                            name='slug'
                            control={control}
                            width={'30%'}
                            maxlength='50'
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
                                <Button variant='contained' component={Link} to={`/accessories/categories/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </form>}
        </>

    )


}

export default UpdateAccessoriesCategory