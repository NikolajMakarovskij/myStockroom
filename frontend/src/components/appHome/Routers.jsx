import React from "react";
import {createBrowserRouter} from "react-router-dom";
import Home from "./Home";
import IndexWorkplace from "../appWorkplace/IndexWorkplace";
import HomeWorkplace from "../appWorkplace/Workplaces/HomeWorkplace";
import HomeRoom from "../appWorkplace/Rooms/HomeRoom";
import NavBar from "./NavBar";

const customWidth = 200
const Routers = createBrowserRouter([
    {path : "/", element: [<NavBar drawerWidth={customWidth} content={<Home/>}/> ],},
    {path: "/workplace", element: [<NavBar drawerWidth={customWidth} content={<IndexWorkplace/>}/>],},
    {path: "/workplace/list", element: [<NavBar drawerWidth={customWidth} content={<HomeWorkplace/>}/>],},
    {path: "/room/list", element: [<NavBar drawerWidth={customWidth} content={<HomeRoom/>}/>],},
]);

export {Routers}