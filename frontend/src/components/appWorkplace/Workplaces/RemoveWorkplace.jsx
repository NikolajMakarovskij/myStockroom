import {React, useEffect, useState, useCallback} from 'react'
import { Box, Button, Typography} from '@mui/material'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate,useParams,Link} from "react-router-dom";
import LinearIndeterminate from "../../appHome/ProgressBar";
import useCSRF from "../../Hooks/CSRF";
import PrintError from "../../Errors/Error.jsx";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const RemoveWorkplace = () => {
    const CSRF = useCSRF()
    const workplaceParam = useParams()
    const workplaceId = workplaceParam.id
    const [workplace, setWorkplaces] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [errorEdit, setErrorEdit] = useState(false)

    const GetData = useCallback(async () => {
        try {
            await AxiosInstanse.get(`workplace/workplace/${workplaceId}/`).then((res) => {
                setWorkplaces(res.data)
            })
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false)
        }

    })

    useEffect(() =>{
        GetData();
    },)

    const navigate = useNavigate()


    const submission = (data) => {
        AxiosInstanse.delete(`workplace/workplace/${workplaceId}/`,{
            headers: {
                    'X-CSRFToken': CSRF
                }
            })
        .then((res) => {
            navigate(`/workplace/list`)
        }).catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    }
    return(
            <>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Удалить кабинет № {
                            loading ? <LinearIndeterminate/> :
                                error ? <PrintError error={error}/>
                                    :workplace.name
                        }
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column',}}>
                    <Box sx={{display:'flex',justifyContent:'space-around', marginBottom:'40px'}}>
                        <ThemeProvider theme={darkTheme} >
                            <Typography>
                                Вы уверены, что хотите удалить кабинет № {
                                        loading ? <LinearIndeterminate/> :
                                            error ? <PrintError error={error}/>
                                                :workplace.name
                                    }?
                            </Typography>
                        </ThemeProvider>
                    </Box>
                    {!errorEdit ? <></> :
                        <Box sx={{display:'flex',justifyContent:'space-around', marginBottom:'40px'}}>
                            <PrintError error={errorEdit}/>
                        </Box>
                    }
                    <ThemeProvider theme={darkTheme}>
                        <Box
                            display="flex"
                            justifyContent="space-between"
                            alignItems="center"
                            marginTop='20px'
                        >
                            <Button variant='contained' color='error' onClick={submission}>Удалить</Button>
                            <Button variant='contained' component={Link} to={`/workplace/list`}>Отмена</Button>
                        </Box>
                    </ThemeProvider>
                </Box>
            </>

    )


}

export default RemoveWorkplace