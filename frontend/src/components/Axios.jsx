import axios from 'axios'

function getApiUrl() {
  const DEBUG = import.meta.env.REACT_APP_DEBUG
  let baseUrl
  if (DEBUG) {
    baseUrl = 'http://localhost/api/'
  } else {
    baseUrl = toString(import.meta.env.REACT_APP_API_URL)
  }
  console.log(baseUrl)
  return baseUrl
}

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

const AxiosInstanse = axios.create({
  baseURL: 'http://0.0.0.0/api/', // TODO change to getApiUrl()
  timeout: 5000,
  headers: {
    'Content-type': 'Application/json',
    accept: 'Application/json',
  },
})

export default AxiosInstanse
