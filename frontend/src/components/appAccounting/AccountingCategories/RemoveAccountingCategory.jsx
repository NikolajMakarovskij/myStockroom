import {React, useEffect, useState, useCallback} from 'react'
import { Box, Button, Typography} from '@mui/material'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate,useParams,Link} from "react-router-dom";
import LinearIndeterminate from "../../appHome/ProgressBar";
import useCSRF from "../../Hooks/CSRF.jsx";
import PrintError from "../../Errors/Error.jsx";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const RemoveAccountingCategory = () => {
    const CSRF = useCSRF()
    const catParam = useParams()
    const catId = catParam.id
    const [category, setCategory] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [errorEdit, setErrorEdit] = useState(false)

    const GetData = useCallback(async () => {
        try {
            await AxiosInstanse.get(`accounting/accounting_category/${catId}/`).then((res) => {
                setCategory(res.data)
            })
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false)
        }
    });

    useEffect(() =>{
        GetData();
    },[]);

    const navigate = useNavigate()


    const submission = () => {
        AxiosInstanse.delete(`accounting/accounting_category/${catId}/`,{
            headers: {
                    'X-CSRFToken': CSRF
                }
            })
        .then(() => {
            navigate(`/accounting/categories/list`)
        }).catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    }
    return(
        <>
            <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                <Typography>
                    Удалить группу {
                        loading ? <LinearIndeterminate/> :
                            error ? <PrintError error={error}/>
                                :category.name
                    }
                </Typography>
            </Box>
            <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column',}}>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <ThemeProvider theme={darkTheme}>
                        <Typography>
                            Вы уверены, что хотите удалить группу {
                                loading ? <LinearIndeterminate/> :
                                    error ? <PrintError error={error}/>
                                        :category.name
                            }?
                        </Typography>
                    </ThemeProvider>
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
                            marginTop='20px'
                        >
                            <Button variant='contained' color='error' onClick={submission}>Удалить</Button>
                            <Button variant='contained' component={Link} to={`/accounting/categories/list`}>Отмена</Button>
                        </Box>
                    </ThemeProvider>
                </Box>
            </Box>
        </>
    )
}

export default RemoveAccountingCategory