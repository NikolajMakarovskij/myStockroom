import React  from 'react';
import {useEffect, useState} from "react";
import {Button, Form, FormGroup, Input, Label} from "reactstrap";
import axios from "axios";
import {API_URL} from "../../../index";

const FormWorkplace = (props) => {
    const [results, setWorkplaces] = useState({})

    const onChange = (e) => {
        const newState = results
        if (e.target.name === "file") {
            newState[e.target.name] = e.target.files[0]
        } else newState[e.target.name] = e.target.value
        setWorkplaces(newState)
    }

    useEffect(() => {
        if (!props.newWorkplace) {
            setWorkplaces(Workplace => props.workplaces)
        }
        // eslint-disable-next-line
    }, [props.workplaces])

    const defaultIfEmpty = value => {
        return value === "" ? "" : value;
    }

    const submitDataEdit = async (e) => {
        e.preventDefault();
        // eslint-disable-next-line
        const result = await axios.put(API_URL + 'workplace/api/v1/workplace/' + results.id + '/', results,
            {headers: {'Content-Type': 'multipart/form-data'}})
            .then(() => {
                props.resetState()
                props.toggle()
            })
    }
    const submitDataAdd = async (e) => {
        e.preventDefault();
        const data = {
            name: results['name'],
            results: results['results']
        }
        // eslint-disable-next-line
        const result = await axios.post(API_URL + 'workplace/api/v1/workplace/', data,
            {headers: {'Content-Type': 'multipart/form-data'}})
            .then(() => {
                props.resetState()
                props.toggle()
            })
    }
    return (
        <Form onSubmit={props.newWorkplace ? submitDataAdd : submitDataEdit}>
            <FormGroup>
                <Label for="name">Рабочее место:</Label>
                <Input
                    type="text"
                    name="name"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(results.name)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="room">Кабинет:</Label>
                <Input
                    type="object"
                    name="room"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(results.room)}
                />
            </FormGroup>
            <div style={{display: "flex", justifyContent: "space-between"}}>
                <Button>Отправить</Button> <Button onClick={props.toggle}>Отмена</Button>
            </div>
        </Form>
    )
}

export default FormWorkplace;