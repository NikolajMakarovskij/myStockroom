import React, {Fragment, useState} from "react";
import {Button, Modal, ModalHeader, ModalBody} from "reactstrap";
import RoomForm from "../appForms/RoomForm";

const ModalRoom = (props) => {
    const [visible, setVisible] = useState(false)
    var button = <Button onClick={() => toggle()}>Редактировать</Button>;

    const toggle = () => {
        setVisible(!visible)
    }

    if (props.create) {
        button = (
            <Button
                color="success"
                className="float-right"
                onClick={() => toggle()}
                style={{minWidth: "200px"}}>
                Добавить комнату
            </Button>
        )
    }
    return (
        <Fragment>
            {button}
            <Modal isOpen={visible} toggle={toggle}>
                <ModalHeader
                    style={{justifyContent: "center"}}>{props.create ? "Добавить комнату" : "Редактировать комнату"}</ModalHeader>
                <ModalBody>
                    <RoomForm
                        room={props.room ? props.room : []}
                        resetState={props.resetState}
                        toggle={toggle}
                        newRoom={props.newRoom}
                    />
                </ModalBody>
            </Modal>
        </Fragment>
    )
}
export default ModalRoom;