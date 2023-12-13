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
            setWorkplaces(Workplace => props.Workplace)
        }
        // eslint-disable-next-line
    }, [props.Workplace])

    const defaultIfEmpty = value => {
        return value === "" ? "" : value;
    }

    const submitDataEdit = async (e) => {
        e.preventDefault();
        // eslint-disable-next-line
        const result = await axios.put(API_URL + Workplace.id, Workplace, {headers: {'Content-Type': 'multipart/form-data'}})
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
        const result = await axios.post(API_URL, data, {headers: {'Content-Type': 'multipart/form-data'}})
            .then(() => {
                props.resetState()
                props.toggle()
            })
    }
    return (
        <Form onSubmit={props.newWorkplace ? submitDataAdd : submitDataEdit}>
            <FormGroup>
                <Label for="name">Кабинет:</Label>
                <Input
                    type="text"
                    name="name"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(results.name)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="floor">Этаж:</Label>
                <Input
                    type="floor"
                    name="floor"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(results.floor)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="building">Здание:</Label>
                <Input
                    type="buildingr"
                    name="building"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(results.building)}
                />
            </FormGroup>
            <div style={{display: "flex", justifyContent: "space-between"}}>
                <Button>Send</Button> <Button onClick={props.toggle}>Cancel</Button>
            </div>
        </Form>
    )
}

export default FormWorkplace;