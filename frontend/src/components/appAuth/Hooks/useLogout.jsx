import AxiosInstanse from '../../Axios.jsx'
import { useCallback } from 'react'

export default function useLogout() {
  const Logout = useCallback(async () => {
    await AxiosInstanse.get(`logout/`)
      .then(() => {
        window.location.href = `/`
      })
      .catch((err) => {
        console.log(err)
      })
  })
  return Logout
}
