import axios from 'axios'

const baseUrl = 'http://localhost/api/'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

const AxiosInstanse = axios.create({
  baseURL: baseUrl,
  timeout: 5000,
  headers: {
    'Content-type': 'Application/json',
    accept: 'Application/json',
  },
})

export default AxiosInstanse
