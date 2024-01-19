import React from "react";
import {createBrowserRouter} from "react-router-dom";
import Home from "./Home";
import IndexWorkplace from "../appWorkplace/IndexWorkplace";
import ListWorkplace from "../appWorkplace/Workplaces/ListWorkplace";
import ListRoom from "../appWorkplace/Rooms/ListRoom";
import NavBar from "./NavBar";
import AuthApp from "../appAuth/AuthApp.jsx";
import CreateRoom from "../appWorkplace/Rooms/CreateRoom";
import UpdateRoom from "../appWorkplace/Rooms/UpdateRoom";
import RemoveRoom from "../appWorkplace/Rooms/RemoveRoom";
import CreateWorkplace from "../appWorkplace/Workplaces/CreateWorkplace";
import UpdateWorkplace from "../appWorkplace/Workplaces/UpdateWorkplace";
import RemoveWorkplace from "../appWorkplace/Workplaces/RemoveWorkplace";
import ListDevice from "../appDevice/ListDevice.jsx";
import IndexStock from "../appStock/IndexStock.jsx";
import ListStockDevices from "../appStock/Devices/ListStockDevices.jsx";

const customWidth = 200
const Routers = createBrowserRouter([
    {path : "/", element: [<NavBar drawerWidth={customWidth} content={<Home/>}/> ],},
    {path : "/auth", element: [<NavBar drawerWidth={customWidth} content={<AuthApp/>}/> ],},
    {path: "/workplace", element: [<NavBar drawerWidth={customWidth} content={<IndexWorkplace/>}/>],},
    {path: "/workplace/list", element: [<NavBar drawerWidth={customWidth} content={<ListWorkplace/>}/>],},
    {path: "/workplace/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateWorkplace/>}/>],},
    {path: "/workplace/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateWorkplace/>}/>],},
    {path: "/workplace/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveWorkplace/>}/>],},
    {path: "/room/list", element: [<NavBar drawerWidth={customWidth} content={<ListRoom/>}/>],},
    {path: "/room/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateRoom/>}/>],},
    {path: "/room/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateRoom/>}/>],},
    {path: "/room/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveRoom/>}/>],},
    {path: "/device/list", element: [<NavBar drawerWidth={customWidth} content={<ListDevice/>}/>],},
    //{path: "/room/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateRoom/>}/>],},
    //{path: "/room/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateRoom/>}/>],},
    //{path: "/room/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveRoom/>}/>],},
    {path: "/stock", element: [<NavBar drawerWidth={customWidth} content={<IndexStock/>}/>],},
    {path: "/stock/device/list", element: [<NavBar drawerWidth={customWidth} content={<ListStockDevices/>}/>],},
    {path: "/stock/device/list/:slug", element: [<NavBar drawerWidth={customWidth} content={<ListStockDevices/>}/>],},
    //{path: "/room/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateRoom/>}/>],},
    //{path: "/room/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateRoom/>}/>],},
    //{path: "/room/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveRoom/>}/>],},
]);

export {Routers}