import React from "react";
import {createBrowserRouter} from "react-router-dom";
import Home from "./Home";
import NavBar from "./NavBar";
import IndexWorkplace from "../appWorkplace/IndexWorkplace";
import ListWorkplace from "../appWorkplace/Workplaces/ListWorkplace";
import CreateWorkplace from "../appWorkplace/Workplaces/CreateWorkplace";
import UpdateWorkplace from "../appWorkplace/Workplaces/UpdateWorkplace";
import RemoveWorkplace from "../appWorkplace/Workplaces/RemoveWorkplace";
import ListRoom from "../appWorkplace/Rooms/ListRoom";
import CreateRoom from "../appWorkplace/Rooms/CreateRoom";
import UpdateRoom from "../appWorkplace/Rooms/UpdateRoom";
import RemoveRoom from "../appWorkplace/Rooms/RemoveRoom";
import IndexEmployee from "../appEmployee/IndexEmployee";
import ListDepartament from "../appEmployee/Departament/ListDepartament";
import CreateDepartament from "../appEmployee/Departament/CreateDepartament";
import RemoveDepartament from "../appEmployee/Departament/RemoveDepartament";
import UpdateDepartament from "../appEmployee/Departament/UpdateDepartament";
import ListPost from "../appEmployee/Post/ListPost";
import CreatePost from "../appEmployee/Post/CreatePost";
import RemovePost from "../appEmployee/Post/RemovePost";
import UpdatePost from "../appEmployee/Post/UpdatePost";
import ListEmployee from "../appEmployee/Employee/ListEmployee";
import CreateEmployee from "../appEmployee/Employee/CreateEmployee";
import UpdateEmployee from "../appEmployee/Employee/UpdateEmployee";
import RemoveEmployee from "../appEmployee/Employee/RemoveEmployee";
import ListDevice from "../appDevice/ListDevice";
import IndexStock from "../appStock/IndexStock";
import ListStockDevices from "../appStock/Devices/ListStockDevices";
import IndexCounterparty from "../appCounterparty/IndexCounterparty";
import ListManufacturer from "../appCounterparty/appManufacturer/ListManufacturer";
import CreateManufacturer from "../appCounterparty/appManufacturer/CreateManufacturer";
import RemoveManufacturer from "../appCounterparty/appManufacturer/RemoveManufacturer";
import UpdateManufacturer from "../appCounterparty/appManufacturer/UpdateManufacturer";
import IndexConsumables from "../appConsumables/IndexConsumables";
import ListConsumables from "../appConsumables/Consumables/ListConsumables";
import ListAccessories from "../appConsumables/Accounting/ListAccessories";

const customWidth = 200
const Routers = createBrowserRouter([
    //Home
    {path : "/", element: [<NavBar drawerWidth={customWidth} content={<Home/>}/> ],},
    //Workplace
    {path: "/workplace", element: [<NavBar drawerWidth={customWidth} content={<IndexWorkplace/>}/>],},
    {path: "/workplace/list", element: [<NavBar drawerWidth={customWidth} content={<ListWorkplace/>}/>],},
    {path: "/workplace/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateWorkplace/>}/>],},
    {path: "/workplace/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateWorkplace/>}/>],},
    {path: "/workplace/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveWorkplace/>}/>],},
    {path: "/room/list", element: [<NavBar drawerWidth={customWidth} content={<ListRoom/>}/>],},
    {path: "/room/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateRoom/>}/>],},
    {path: "/room/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateRoom/>}/>],},
    {path: "/room/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveRoom/>}/>],},
    //Employee
    {path: "/employee", element: [<NavBar drawerWidth={customWidth} content={<IndexEmployee/>}/>],},
    {path: "/employee/list", element: [<NavBar drawerWidth={customWidth} content={<ListEmployee/>}/>],},
    {path: "/employee/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateEmployee/>}/>],},
    {path: "/employee/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateEmployee/>}/>],},
    {path: "/employee/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveEmployee/>}/>],},
    {path: "/departament/list", element: [<NavBar drawerWidth={customWidth} content={<ListDepartament/>}/>],},
    {path: "/departament/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateDepartament/>}/>],},
    {path: "/departament/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateDepartament/>}/>],},
    {path: "/departament/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveDepartament/>}/>],},
    {path: "/post/list", element: [<NavBar drawerWidth={customWidth} content={<ListPost/>}/>],},
    {path: "/post/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreatePost/>}/>],},
    {path: "/post/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdatePost/>}/>],},
    {path: "/post/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemovePost/>}/>],},
    //Counterparty
    {path: "/counterparty", element: [<NavBar drawerWidth={customWidth} content={<IndexCounterparty/>}/>],},
    {path: "/counterparty/manufacturer/list", element: [<NavBar drawerWidth={customWidth} content={<ListManufacturer/>}/>],},
    {path: "/counterparty/manufacturer/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateManufacturer/>}/>],},
    {path: "/counterparty/manufacturer/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateManufacturer/>}/>],},
    {path: "/counterparty/manufacturer/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveManufacturer/>}/>],},
    //Consumables
    {path: "/consumables", element: [<NavBar drawerWidth={customWidth} content={<IndexConsumables/>}/>],},
    {path: "/consumables/list", element: [<NavBar drawerWidth={customWidth} content={<ListConsumables/>}/>],},
    {path: "/accessories/list", element: [<NavBar drawerWidth={customWidth} content={<ListAccessories/>}/>],},
    //Device
    {path: "/device/list", element: [<NavBar drawerWidth={customWidth} content={<ListDevice/>}/>],},
    //{path: "/device/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateRoom/>}/>],},
    //{path: "/device/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateRoom/>}/>],},
    //{path: "/device/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveRoom/>}/>],},
    //Stock
    {path: "/stock", element: [<NavBar drawerWidth={customWidth} content={<IndexStock/>}/>],},
    {path: "/stock/device/list", element: [<NavBar drawerWidth={customWidth} content={<ListStockDevices/>}/>],},
    {path: "/stock/device/list/:slug", element: [<NavBar drawerWidth={customWidth} content={<ListStockDevices/>}/>],},
    //{path: "/stock/device/list/create", element: [<NavBar drawerWidth={customWidth} content={<CreateRoom/>}/>],},
    //{path: "/stock/device/list/edit/:id", element: [<NavBar drawerWidth={customWidth} content={<UpdateRoom/>}/>],},
    //{path: "/stock/device/list/remove/:id", element: [<NavBar drawerWidth={customWidth} content={<RemoveRoom/>}/>],},
]);

export {Routers}