import AxiosInstanse from "../../Axios.jsx";
import {useCallback} from 'react'


export default function useLogout() {

        const Logout = useCallback(async () => {
            await AxiosInstanse.get(`logout/`)
                .then((res) => {
                    window.location.href=(`/`);
                })
                .catch((err) => {
                    console.log(err);
                });
        })
    return Logout
}