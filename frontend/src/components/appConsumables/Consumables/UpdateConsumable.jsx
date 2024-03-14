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
import AutocompleteField from "../../Forms/AutocompleteField.jsx";
import useInterval from "../../Hooks/useInterval";
import useCSRF from "../../Hooks/CSRF.jsx";
import PrintError from "../../Errors/Error.jsx";
import MultilineField from "../../Forms/MultilineField.jsx";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const UpdateConsumable = () => {
    const CSRF = useCSRF()
    const conParam = useParams()
    const conId = conParam.id
    const [cat, setCat] = useState()
    const [MF, setMF] = useState()
    const [consumable, setConsumable] = useState()
    const [loading, setLoading] = useState(true)
    const [loadingMF, setLoadingMF] = useState(true)
    const [loadingCat, setLoadingCat] = useState(true)
    const [errorData, setErrorData] = useState(false)
    const [errorMF, setErrorMF] = useState(false)
    const [errorCat, setErrorCat] = useState(false)
    const [errorEdit, setErrorEdit] = useState(false)
    const [delay, setDelay] = useState(100)
    const navigate = useNavigate()


    useInterval(() => {
        async function getCategory() {
            try {
                await AxiosInstanse.get(`consumables/consumable_category/`).then((res) => {
                    setCat(res.data)
                    setErrorCat(null)
                    setDelay(5000)
                })
              } catch (error) {
                    setErrorCat(error.message);
                    setDelay(null)
              } finally {
                    setLoadingCat(false);
              }
        }
        async function getMF() {
            try {
                await AxiosInstanse.get(`counterparty/manufacturer/`).then((res) => {
                    setMF(res.data)
                    setErrorMF(null)
                    setDelay(5000)
                })
              } catch (error) {
                    setErrorMF(error.message);
                    setDelay(null)
              } finally {
                    setLoadingMF(false);
              }
        }
        Promise.all([getCategory(), getMF()])
    }, delay);


    async function getCurrentData() {
        try {
            await AxiosInstanse.get(`consumables/consumable/${conId}/`).then((res) => {
                setConsumable(res.data)
                setValue('name', res.data.name)
                setValue('categories', res.data.categories)
                setValue('serial', res.data.serial)
                setValue('invent', res.data.invent)
                setValue('manufacturer', res.data.manufacturer)
                setValue('description', res.data.description)
                setValue('note', res.data.note)
                setErrorData(false)
            })
        } catch (error) {
            setErrorData(error.message);
            setDelay(null)
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        getCurrentData()
    }, []);

    const defaultValues = {
        name: '',
        categories: '',
        serial: '',
        invent: '',
        manufacturer: '',
        description: '',
        note: ''
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле').max(150, 'Должно быть короче 150 символов'),
            serial: yup.string().max(50, 'Должно быть короче 50 символов'),
            invent: yup.string().max(50, 'Должно быть короче 50 символов'),
            description: yup.string().max(1000, 'Должно быть короче 1000 символов'),
            note: yup.string().max(1000, 'Должно быть короче 1000 символов')
        })
      .required()

    const {
        handleSubmit,
        setValue,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})
    const submission = (data) => {
        AxiosInstanse.put(`consumables/consumable/${conId}/`,{
                name: data.name,
                categories: data.categories,
                serial: data.serial,
                invent: data.invent,
                manufacturer: data.manufacturer,
                description: data.description,
                note: data.note
        },{
            headers: {
                    'X-CSRFToken': CSRF
                }
        })
        .then((res) => {
            navigate(`/consumables/list`)
        })
        .catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    }
    return(
        <>
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                         Редактировать расходник {loading ? <LinearIndeterminate/> :
                             errorData ? <PrintError error={errorData}/>
                                 :` ${consumable.name}`
                        }
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>

                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Расходник'
                            placeholder='Введите название расходника'
                            name='name'
                            control={control}
                            width={'30%'}
                            maxlength='150'
                        />
                        <AutocompleteField
                            loading={loadingCat}
                            error={errorCat}
                            name='categories'
                            control={control}
                            width={'30%'}
                            options={cat}
                            label='Выберите группу'
                            placeholder='Выберите группу'
                            noOptionsText='Группы не обнаружены'
                            optionLabel={(option) => `${option.name}`}
                        />
                        <AutocompleteField
                            loading={loadingMF}
                            error={errorMF}
                            name='manufacturer'
                            control={control}
                            width={'30%'}
                            options={MF}
                            label='Выберите производителя'
                            placeholder='Выберите производителя'
                            noOptionsText='Производители не обнаружены'
                            optionLabel={(option) => `${option.name}`}
                        />
                    </Box>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Серийный №'
                            placeholder='Введите Серийный №'
                            name='serial'
                            control={control}
                            width={'30%'}
                            maxlength='50'
                        />
                        <CustomTextField
                            label='Инвентарный №'
                            placeholder='Введите инвентарный №'
                            name='invent'
                            control={control}
                            width={'30%'}
                            maxlength='50'
                        />
                    </Box>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <MultilineField
                            label='Описание'
                            placeholder='Введите описание'
                            name='description'
                            control={control}
                            width={'30%'}
                            rows={4}
                            maxlength='1000'
                        />
                        <MultilineField
                            label='Примечание'
                            placeholder='Введите примечание'
                            name='note'
                            control={control}
                            width={'30%'}
                            rows={4}
                            maxlength='1000'
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
                                <Button variant='contained' component={Link} to={`/consumables/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </form>
        </>

    )


}

export default UpdateConsumable