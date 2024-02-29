import {React, useEffect, useState, useCallback} from 'react'
import { Box, Button, Typography} from '@mui/material'
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate,useParams,Link} from "react-router-dom";
import LinearIndeterminate from "../../appHome/ProgressBar";

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const RemoveWorkplace = () => {
    const workplaceParam = useParams()
    const workplaceId = workplaceParam.id
    const [workplace, setWorkplaces] = useState()
    const [loading, setLoading] = useState(true)

    const GetData = useCallback(async () => {
        await AxiosInstanse.get(`workplace/workplace/${workplaceId}/`).then((res) => {
            setWorkplaces(res.data)
            setLoading(false)
        })
    })

    useEffect(() =>{
        GetData();
    },)

    const navigate = useNavigate()


    const submission = (data) => {
        AxiosInstanse.delete(`workplace/workplace/${workplaceId}/`)
        .then((res) => {
            navigate(`/workplace/list`)
        })
    }
    return(
        <>
            {loading ? <LinearIndeterminate/> :
            <>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Удалить кабинет № {workplace.name}
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column',}}>
                    <ThemeProvider theme={darkTheme}>
                        <Typography>
                            Вы уверены, что хотите удалить кабинет № {workplace.name}?
                        </Typography>
                    </ThemeProvider>
                    <Box>
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
                </Box>
            </>}
        </>

    )


}

export default RemoveWorkplace