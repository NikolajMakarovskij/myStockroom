import { useEffect, useState } from 'react'
import AxiosInstanse from '../Axios.jsx'

export default function useCSRF() {
  const [csrf, setCsrf] = useState()

  const getCSRF = () => {
    AxiosInstanse.get('csrf/', {
      credentials: 'include',
    })
      .then((res) => {
        setCsrf(res.headers.get('X-CSRFToken'))
      })
      .catch((err) => {
        console.log(err)
      })
  }

  useEffect(() => {
    getCSRF()
  }, [])

  return csrf
}
