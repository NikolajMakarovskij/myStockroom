import React from "react";
import {Fragment, useState} from "react";
import {Button, Modal, ModalHeader, ModalFooter} from "reactstrap";
import axios from "axios";
import {API_URL} from "../../../index";
import {Link } from "react-router-dom";

const RemoveWorkplace = (props) => {
    const [visible, setVisible] = useState(false)
    const toggle = () => {
        setVisible(!visible)
    }
    const deleteWorkplace = () => {
        axios.delete(API_URL + 'workplace/api/v1/workplace/' + props.id + '/').then(() => {
            props.resetState()
            toggle();
        });
    }
    return (
        <Fragment>
            <Link color="danger" onClick={() => toggle()}>
                Удалить
            </Link>
            <Modal isOpen={visible} toggle={toggle} style={{width: "300px", marginTop: "80px"}}>
                <ModalHeader style={{justifyContent: "center"}}>Вы уверены?</ModalHeader>
                <ModalFooter style={{display: "flex", justifyContent: "space-between"}}>
                    <Button
                        type="button"
                        onClick={() => deleteWorkplace()}
                        color="secondary"
                    >Удалить</Button>
                    <Button type="button" onClick={() => toggle()}>Отмена</Button>
                </ModalFooter>
            </Modal>
        </Fragment>
    )
}
export default RemoveWorkplace;