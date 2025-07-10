import axios from 'axios'

function getApiUrl() {
  const DEV = import.meta.env.DEV
  let baseUrl
  if (DEV) {
    baseUrl = 'http://localhost/api/'
  } else {
    baseUrl = `http://${import.meta.env.VITE_BASE_URL}/api/`
  }
  console.log(baseUrl)
  return baseUrl
}

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

const AxiosInstanse = axios.create({
  baseURL: getApiUrl(),
  timeout: 30000,
  headers: {
    'Content-type': 'Application/json',
    accept: 'Application/json',
  },
})

export default AxiosInstanse
