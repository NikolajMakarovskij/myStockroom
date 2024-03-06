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

const RemoveEmployee = () => {
    const CSRF = useCSRF()
    const emplParam = useParams()
    const emplId = emplParam.id
    const [empl, setEmpl ] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(false)
    const [errorEdit, setErrorEdit] = useState(false)


    const GetData = useCallback(async () => {
        try {
            await AxiosInstanse.get(`employee/employee/${emplId}/`).then((res) => {
                setEmpl(res.data)
            })
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false)
        }
    });

    useEffect(() =>{
        GetData();
    },)

    const navigate = useNavigate()

    const submission = (data) => {
        AxiosInstanse.delete(`employee/employee/${emplId}/`,{
            headers: {
                    'X-CSRFToken': CSRF
                }
        })
        .then((res) => {
            navigate(`/employee/list`)
        })
        .catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    }
    return(
            <>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Удалить сотрудника {
                        loading ? <LinearIndeterminate/> :
                            error ? <PrintError error={error}/>
                                :` ${empl.surname} ${empl.name} ${empl.last_name}`
                        }
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column',}}>
                    <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                        <ThemeProvider theme={darkTheme}>
                            <Typography>
                                Вы уверены, что хотите удалить сотрудника {loading ? <LinearIndeterminate/> :
                                    error ? <PrintError error={error}/>
                                        :` ${empl.surname} ${empl.name} ${empl.last_name}`
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
                                <Button variant='contained' component={Link} to={`/employee/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </>
    )
}

export default RemoveEmployee