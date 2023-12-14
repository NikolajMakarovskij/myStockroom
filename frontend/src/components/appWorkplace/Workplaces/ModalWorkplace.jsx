import React  from 'react';
import {Fragment, useState} from "react";
import {Modal, ModalHeader, ModalBody} from "reactstrap";
import WorkplaceForm from "./FormWorkplace";
import {Link } from "react-router-dom";

const ModalWorkplace = (props) => {
    const [visible, setVisible] = useState(false)
    var button = <Link onClick={() => toggle()}>Редактировать</Link>;

    const toggle = () => {
        setVisible(!visible)
    }

    if (props.create) {
        button = (
            <Link
                color="secondary"
                className="float-right"
                onClick={() => toggle()}
                style={{minWidth: "200px"}}>
                Добавить
            </Link>
        )
    }
    return (
        <Fragment  >
            {button}
            <Modal style={{marginTop: "80px"}} isOpen={visible} toggle={toggle}>
                <ModalHeader
                    style={{justifyContent: "center" }}>{props.create ? "Добавить" : "Редактировать"}</ModalHeader>
                <ModalBody>
                    <WorkplaceForm
                        results={props.results ? props.results : []}
                        resetState={props.resetState}
                        toggle={toggle}
                        newWorkplace={props.newWorkplace}
                    />
                </ModalBody>
            </Modal>
        </Fragment>
    )
}
export default ModalWorkplace;