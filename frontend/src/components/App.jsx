import './App.css';
import React  from 'react';
import {Fragment,} from "react";
import {RouterProvider} from "react-router-dom";
import {Routers} from "./appHome/Routers"



function App() {
        return (
        <Fragment>
            <RouterProvider router={Routers} />
        </Fragment>
        );
    }

        export default App;
