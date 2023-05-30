import {Container, Row, Col} from "reactstrap";
import ListRooms from "../appWorkplace/appLists/RoomList";
import axios from "axios";
import React, {useEffect, useState} from "react";
import ModalRooms from "../appWorkplace/appModals/RoomModal";
import {API_URL_ROOM} from "../../index";

const Home = () => {
    const [rooms, setRooms] = useState([])

    useEffect(()=>{
        getRooms()
    },[])

    const getRooms = (data)=>{
        axios.get(API_URL_ROOM).then(data => setRooms(data.data))
    }

    const resetState = () => {
        getRooms();
    };

    return (
        <Container style={{marginTop: "20px"}}>
            <Row>
                <Col>
                    <ListRooms rooms={rooms} resetState={resetState} newRoom={false}/>
                </Col>
            </Row>

        </Container>
    )
}

export default Home;
