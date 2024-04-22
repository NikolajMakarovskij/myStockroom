import {React, useState, useEffect, useCallback} from 'react'
import { Box, Button, Typography, TextField} from '@mui/material'
import CustomTextField from "../../Forms/TextField";
import {useForm} from 'react-hook-form'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate, Link} from "react-router-dom";
import * as yup from "yup";
import {yupResolver} from "@hookform/resolvers/yup";
import AutocompleteField from "../../Forms/AutocompleteField";
import useInterval from "../../Hooks/useInterval";
import useCSRF from "../../Hooks/CSRF.jsx";
import PrintError from "../../Errors/Error.jsx";
import MultilineField from "../../Forms/MultilineField.jsx";
import AutocompleteMultipleField from "../../Forms/AutocompleteMultipleField";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const options = []

const CreateDevice = () => {
    const CSRF = useCSRF()
    const [category, setCategory] = useState('')
    const [MF, setMF] = useState()
    const [cons, setCons] = useState()
    const [acc, setAcc] = useState()
    const [value, setValues] = useState(options.id)
    const [loadingCategory, setLoadingCategory] = useState(true)
    const [loadingMF, setLoadingMF] = useState(true)
    const [loadingCons, setLoadingCons] = useState(true)
    const [loadingAcc, setLoadingAcc] = useState(true)
    const [errorCategory, setErrorCategory] = useState(null)
    const [errorMF, setErrorMF] = useState(null)
    const [errorCons, setErrorCons] = useState(null)
    const [errorAcc, setErrorAcc] = useState(null)
    const [errorEdit, setErrorEdit] = useState(null)
    const [delay, setDelay] = useState(100)
    const navigate = useNavigate()

    useInterval(() => {
        async function getCategory() {
            try {
                await AxiosInstanse.get(`device/device_cat/`).then((res) => {
                    setCategory(res.data)
                    setErrorCategory(null)
                    setDelay(500000)
                })
              } catch (error) {
                    setErrorCategory(error.message);
                    setDelay(null)
              } finally {
                    setLoadingCategory(false);
              }
        }
        async function getMF() {
            try {
                await AxiosInstanse.get(`counterparty/manufacturer/`).then((res) => {
                    setMF(res.data)
                    setErrorMF(null)
                    setDelay(500000)
                })
              } catch (error) {
                    setErrorMF(error.message);
                    setDelay(null)
              } finally {
                    setLoadingMF(false);
              }
        }
        async function getConsumables() {
            try {
                await AxiosInstanse.get(`consumables/consumable_list/`).then((res) => {
                    setCons(res.data)
                    setErrorCons(null)
                    setDelay(500000)
                })
              } catch (error) {
                    setErrorCons(error.message);
                    setDelay(null)
              } finally {
                    setLoadingCons(false);
              }
        }
        async function getAccessories() {
            try {
                await AxiosInstanse.get(`consumables/accessories_list/`).then((res) => {
                    setAcc(res.data)
                    setErrorAcc(null)
                    setDelay(500000)
                })
              } catch (error) {
                    setErrorAcc(error.message);
                    setDelay(null)
              } finally {
                    setLoadingAcc(false);
              }
        }
        Promise.all([getCategory(), getMF(), getConsumables(), getAccessories()])
    }, delay);

    const defaultValues = {
        name: '',
        hostname: '',
        ip_address: '',
        login: '',
        pwd: '',
        categories: '',
        manufacturer: '',
        serial: '',
        invent: '',
        description: '',
        workplace: '',
        consumable: '',
        accessories: '',
        note: '',
    }

    const schema = yup
        .object({
            name: yup.string().required('Обязательное поле').max(150, 'Должно быть короче 150 символов'),
            hostname: yup.string().max(50, 'Должно быть короче 50 символов'),
            ip_address: yup.string().url('Не является url адресом').max(50, 'Должно быть короче 50 символов'),
            login: yup.string().max(50, 'Должно быть короче 50 символов'),
            pwd: yup.string().max(20, 'Должно быть короче 20 символов'),
            serial: yup.string().max(50, 'Должно быть короче 50 символов'),
            invent: yup.string().max(50, 'Должно быть короче 50 символов'),
            description: yup.string().max(200, 'Должно быть короче 200 символов'),
            note: yup.string().max(1000, 'Должно быть короче 1000 символов'),
        })
      .required()

    const {
        handleSubmit,
        control,
    } = useForm({defaultValues:defaultValues, resolver: yupResolver(schema)})

    const submission =useCallback( (data) => {
        AxiosInstanse.post(`device/device/`,{
                name: data.name,
                hostname: data.hostname,
                ip_address: data.ip_address,
                login: data.login,
                pwd: data.pwd,
                categories: data.categories,
                manufacturer: data.manufacturer,
                serial: data.serial,
                invent: data.invent,
                description: data.description,
                consumable: data.consumable,
                accessories: data.accessories,
                note: data.note,
        },{
            headers: {
                    'X-CSRFToken': CSRF
                }
        })
        .then((res) => {
            navigate(`/device/list`)
        }).catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    })
    return(
        <>
            <form onSubmit={handleSubmit(submission)}>
                <Box sx={{display:'flex', justifyContent:'center',width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Добавить устройство
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column'}}>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Название'
                            placeholder='Введите название'
                            name='name'
                            id='name'
                            control={control}
                            width={'30%'}
                            maxlength='150'
                        />
                        <AutocompleteField
                            loading={loadingCategory}
                            error={errorCategory}
                            name='categories'
                            id='categories'
                            control={control}
                            width={'30%'}
                            options={category}
                            label='Выберите группу'
                            placeholder='Выберите группу'
                            noOptionsText='Группа не обнаружена'
                            optionLabel={(option) => `${option.name}`}
                        />
                        <AutocompleteField
                            loading={loadingMF}
                            error={errorMF}
                            name='manufacturer'
                            id='manufacturer'
                            control={control}
                            width={'30%'}
                            options={MF}
                            label='Выберите производителя'
                            placeholder='Выберите производителя'
                            noOptionsText='Производитель не обнаружен'
                            optionLabel={(option) => `${option.name}`}
                        />
                    </Box>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Серийный №'
                            placeholder='Введите серийный №'
                            name='serial'
                            id='serial'
                            control={control}
                            width={'30%'}
                            maxlength='50'
                        />
                        <CustomTextField
                            label='Инвентарный №'
                            placeholder='Введите инвентарный №'
                            name='invent'
                            id='invent'
                            control={control}
                            width={'30%'}
                            maxlength='50'
                        />
                        <CustomTextField
                            label='Логин'
                            placeholder='Введите логин'
                            name='login'
                            id='login'
                            control={control}
                            width={'30%'}
                            maxlength='50'
                        />
                    </Box>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <CustomTextField
                            label='Имя хоста'
                            placeholder='Введите имя хоста'
                            name='hostname'
                            id='hostname'
                            control={control}
                            width={'30%'}
                            maxlength='50'
                        />
                        <CustomTextField
                            label='IP адрес'
                            placeholder='Введите IP адрес'
                            name='ip_address'
                            id='ip_address'
                            control={control}
                            width={'30%'}
                            maxlength='50'
                        />
                        <CustomTextField
                            label='Пароль'
                            placeholder='Введите пароль'
                            name='pwd'
                            id='pwd'
                            control={control}
                            width={'30%'}
                            maxlength='20'
                        />
                    </Box>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <AutocompleteMultipleField
                            loading={loadingCons}
                            error={errorCons}
                            name='consumable'
                            id='consumable'
                            control={control}
                            width={'30%'}
                            options={cons}
                            label='Выберите расходник'
                            placeholder='Выберите расходник'
                            noOptionsText='Расходник не обнаружен'
                            optionLabel={(option) => `${option.name}`}
                        />
                        <AutocompleteMultipleField
                            loading={loadingAcc}
                            error={errorAcc}
                            name='accessories'
                            id='accessories'
                            control={control}
                            width={'30%'}
                            options={acc}
                            label='Выберите комплектующее'
                            placeholder='Выберите комплектующее'
                            noOptionsText='Комплектующее не обнаружено'
                            optionLabel={(option) => `${option.name}`}
                        />
                    </Box>
                    <Box sx={{display:'flex', width:'100%', justifyContent:'space-around', marginBottom:'40px'}}>
                        <MultilineField
                            label='Описание'
                            placeholder='Введите описание'
                            name='description'
                            id='description'
                            control={control}
                            width={'30%'}
                            rows={4}
                            maxlength='200'
                        />
                        <MultilineField
                            label='Примечание'
                            placeholder='Введите примечание'
                            name='note'
                            id='note'
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
                                <Button variant='contained' component={Link} to={`/device/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </form>
    </>

    )


}

export default CreateDevice
