import React from "react";
import {createBrowserRouter} from "react-router-dom";
import Header from "./appHeader/Header";
import Home from "./appHome/Home";
import IndexWorkplace from "./appWorkplace/IndexWorkplace";
import HomeWorkplace from "./appWorkplace/Workplaces/HomeWorkplace";


const Routers = createBrowserRouter([
    {path : "/", element: [<Header/>, <Home/>],},
    {path: "/workplace", element: [ <Header/>, <IndexWorkplace/>, ],},
    {path: "/workplace/list", element: [ <Header/>, <HomeWorkplace/>, ],},
]);

export {Routers}