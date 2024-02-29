import React from "react";
import { Box, Button, Typography, Grid, TextField} from '@mui/material'
import {createTheme, ThemeProvider} from '@mui/material/styles';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

class LoginApp extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      csrf: "",
      username: "",
      password: "",
      error: "",
      isAuthenticated: false,
    };
  }

  componentDidMount = () => {
    this.getSession();
  }

  getCSRF = () => {
    fetch("http://localhost/api/csrf/", {
      credentials: "include",
    })
    .then((res) => {
      let csrfToken = res.headers.get("X-CSRFToken");
      this.setState({csrf: csrfToken});
      console.log(csrfToken);
    })
    .catch((err) => {
      console.log(err);
    });
  }

  getSession = () => {
    fetch("http://localhost/api/session/", {
      credentials: "include",
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (data.isAuthenticated) {
        this.setState({isAuthenticated: true});
      } else {
        this.setState({isAuthenticated: false});
        this.getCSRF();
      }
    })
    .catch((err) => {
      console.log(err);
    });
  }



  handlePasswordChange = (event) => {
    this.setState({password: event.target.value});
  }

  handleUserNameChange = (event) => {
    this.setState({username: event.target.value});
  }

  isResponseOk(response) {
    if (response.status >= 200 && response.status <= 299) {
      return response.json();
    } else {
      throw Error(response.statusText);
    }
  }

  login = (event) => {
    event.preventDefault();
    fetch("http://localhost/api/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": this.state.csrf,
      },
      credentials: "include",
      body: JSON.stringify({username: this.state.username, password: this.state.password}),
    })
    .then(this.isResponseOk)
    .then((data) => {
      window.location.href=('http://localhost:3000/');
      console.log(data);
      this.setState({isAuthenticated: true, username: "", password: "", error: ""});
    })
    .catch((err) => {
      console.log(err);
      this.setState({error: "Wrong username or password."});
    });
  }

  render() {
      return (
          <Grid
            container
            spacing={0}
            direction="column"
            alignItems="center"
            justifyContent="center"
            sx={{ minHeight: '100vh' }}
          >
          <form onSubmit={this.login} >
            <Box sx={{display:'flex', width:'460px', flexDirection:'column'}}>
              <Box sx={{display:'flex', justifyContent:'space-around', marginBottom:'40px'}}>
                <Typography variant='h5'>
                  Авторизация
                </Typography>
              </Box>
              <TextField
                  id="username"
                  name="username"
                  type="text"
                  className="form-control"
                  label="Имя пользователя"
                  variant="outlined"
                  value={this.state.username}
                  onChange={this.handleUserNameChange}
                  sx={{
                    display:'flex',
                    justifyContent:'space-around',
                    marginBottom:'40px'
                  }}
              />
              <TextField
                  id="password"
                  name="password"
                  type="password"
                  className="form-control"
                  label="Пароль"
                  variant="outlined"
                  value={this.state.password}
                  error={this.state.error}
                  onChange={this.handlePasswordChange}
                  sx={{
                    display:'flex',
                    justifyContent:'space-around',
                    marginBottom:'40px'
                  }}
              />
              <Box sx={{display:'flex',justifyContent:'space-around', marginBottom:'40px'}}>
                <Button variant='contained' type="submit" color='inherit' className="btn btn-primary">
                    Войти
                </Button>
              </Box>
            </Box>
          </form>
          </Grid>
      );
  }
}

export default LoginApp;