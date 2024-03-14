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

const RemoveAccessories = () => {
    const CSRF = useCSRF()
    const conParam = useParams()
    const conId = conParam.id
    const [consumable, setConsumable ] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(false)
    const [errorEdit, setErrorEdit] = useState(false)


    const GetData = useCallback(async () => {
        try {
            await AxiosInstanse.get(`consumables/accessories/${conId}/`).then((res) => {
                setConsumable(res.data)
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
        AxiosInstanse.delete(`consumables/accessories/${conId}/`,{
            headers: {
                    'X-CSRFToken': CSRF
                }
        })
        .then((res) => {
            navigate(`/accessories/list`)
        })
        .catch((error) => {
            setErrorEdit(error.response.data.detail)
        });
    }
    return(
            <>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Удалить комплектующее {
                        loading ? <LinearIndeterminate/> :
                            error ? <PrintError error={error}/>
                                :` ${consumable.name}`
                        }
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column',}}>
                    <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                        <ThemeProvider theme={darkTheme}>
                            <Typography>
                                Вы уверены, что хотите удалить комплектующее {loading ? <LinearIndeterminate/> :
                                    error ? <PrintError error={error}/>
                                        :` ${consumable.name}`
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
                                <Button variant='contained' component={Link} to={`/accessories/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </>
    )
}

export default RemoveAccessories