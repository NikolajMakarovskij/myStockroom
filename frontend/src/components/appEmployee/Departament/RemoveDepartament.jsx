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

const RemoveDepartament = () => {
    const roomParam = useParams()
    const roomId = roomParam.id
    const [room, setRooms] = useState()
    const [loading, setLoading] = useState(true)

    const GetData = () => {
        AxiosInstanse.get(`workplace/room/${roomId}/`).then((res) => {
            setRooms(res.data)
            setLoading(false)
        })
    }

    useEffect(() =>{
        GetData();
    },)

    const navigate = useNavigate()


    const submission = useCallback(async (data) => {
        await AxiosInstanse.delete(`workplace/room/${roomId}/`)
        .then((res) => {
            navigate(`/room/list`)
        })
    })
    return(
        <div>
            {loading ? <LinearIndeterminate/> :
            <div>
                <Box sx={{display:'flex', justifyContent:'center', width:'100%',  marginBottom:'10px'}}>
                    <Typography>
                        Удалить кабинет № {room.name}
                    </Typography>
                </Box>
                <Box sx={{display:'flex', width:'100%', boxShadow:3, padding:4, flexDirection:'column',}}>
                    <ThemeProvider theme={darkTheme}>
                        <Typography>
                            Вы уверены, что хотите удалить кабинет № {room.name}?
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
                                <Button variant='contained' component={Link} to={`/room/list`}>Отмена</Button>
                            </Box>
                        </ThemeProvider>
                    </Box>
                </Box>
            </div>}
        </div>

    )


}

export default RemoveDepartament