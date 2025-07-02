import axios from 'axios'

function getApiUrl() {
  const DEBUG = import.meta.env.REACT_APP_DEBUG
  let baseUrl
  if (DEBUG) {
    baseUrl = 'http://localhost/api/'
  } else {
    baseUrl = import.meta.env.REACT_APP_API_URL
  }
  return baseUrl
}

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

const AxiosInstanse = axios.create({
  baseURL: getApiUrl(),
  timeout: 5000,
  headers: {
    'Content-type': 'Application/json',
    accept: 'Application/json',
  },
})

export default AxiosInstanse
