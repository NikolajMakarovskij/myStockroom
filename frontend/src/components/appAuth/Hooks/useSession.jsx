import AxiosInstanse from "../../Axios.jsx";
import {useState, useCallback, useEffect,} from 'react'


export default function useSession() {
    const [session, setSession ] = useState(
        {
            username: '',
            isAuthenticated: false,
            error: false
        }
    )


    const GetSession = useCallback(async () => {
        await AxiosInstanse.get(`session/`,  )
            .then((res) => {
                if (!res.data.isAuthenticated) {
                    setSession({isAuthenticated: true})
                } else {
                    setSession(
                        {
                            isAuthenticated: res.data.isAuthenticated,
                            username: res.data.username
                        }
                    )

                }
            })
            .catch((error) => {
                setSession({error: error})
                console.log(error)
            })
    })
    useEffect(() =>{
        GetSession();
    },[])

    return (session)
}