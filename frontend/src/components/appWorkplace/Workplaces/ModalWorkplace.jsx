import React  from 'react';
import {Fragment, useState} from "react";
import {Button, Modal, ModalHeader, ModalBody} from "reactstrap";
import WorkplaceForm from "./FormWorkplace";

const ModalWorkplace = (props) => {
    const [visible, setVisible] = useState(false)
    var button = <Button onClick={() => toggle()}>Редактировать</Button>;

    const toggle = () => {
        setVisible(!visible)
    }

    if (props.create) {
        button = (
            <Button
                color="secondary"
                className="float-right"
                onClick={() => toggle()}
                style={{minWidth: "200px"}}>
                Добавить
            </Button>
        )
    }
    return (
        <Fragment>
            {button}
            <Modal isOpen={visible} toggle={toggle}>
                <ModalHeader
                    style={{justifyContent: "center"}}>{props.create ? "Добавить" : "Редактировать"}</ModalHeader>
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