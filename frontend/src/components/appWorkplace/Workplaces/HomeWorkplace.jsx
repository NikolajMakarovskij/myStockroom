import React from "react";
import {Container} from "reactstrap";
import ListWorkplace from "./ListWorkplaces";
import axios from "axios";
import {useEffect, useState} from "react";
import {API_URL} from "../../../index";

const HomeWorkplace = () => {
    const [room, setWorkplaces] = useState([])

    useEffect(()=>{
        getWorkplaces()
    },[])

    const getWorkplaces = (data)=>{
        axios.get(API_URL,
        {headers: '*'}
        ).then(resp => {setWorkplaces(resp.data,
            console.log("Success ========>", resp))
            }
        ).catch(error => {
            console.log("Error ========>", error);
            }
        )
    }

    const resetState = () => {
        getWorkplaces();
    };

    return (
        <Container style={{marginTop: "80px"}}>
            <ListWorkplace room={room} resetState={resetState} newWorkplace={false}/>
        </Container>
    )
}

export default HomeWorkplace;