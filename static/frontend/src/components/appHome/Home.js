import React from "react";
import {Container, Row, Col} from "reactstrap";
import ListWorkplace from "../appWorkplace/ListWorkplaces";
import axios from "axios";
import {useEffect, useState} from "react";
import ModalWorkplace from "../appWorkplace/ModalWorkplace";
import {API_URL} from "../../index";

const Home = () => {
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
        <Container style={{marginTop: "20px"}}>
            <Row>
                <Col>
                    <ListWorkplace room={room} resetState={resetState} newWorkplace={false}/>
                </Col>
            </Row>
            <Row>
                <Col>
                    <ModalWorkplace
                    create={true}
                    resetState={resetState}
                    newWorkplace={true}/>
                </Col>
            </Row>
        </Container>
    )
}

export default Home;