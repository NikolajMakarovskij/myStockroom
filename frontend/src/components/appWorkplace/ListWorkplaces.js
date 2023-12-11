import React  from 'react';
import {Table} from "reactstrap";
import ModalWorkplace from "./ModalWorkplace";
import RemoveWorkplace from "./RemoveWorkplace";

const ListWorkplace = (props) => {
    const {room} = props
    return (
        <Table align-middle caprion-top hover >
            <caption top>Количество комнат {room.length} </caption>
            <thead align="center">
            <tr>
                <th>№ П/П</th>
                <th>Кабинет</th>
                <th>Этаж</th>
                <th>Здание</th>
                <th>Рабочие места</th>
                <th></th>
            </tr>
            </thead>
            <tbody>
            {!room || room.length === 0 ? (
                <tr>
                    <td colSpan="6" align="center">
                        <b>Пока ничего нет</b>
                    </td>
                </tr>
            ) : room.map((results, index) => (
                    <tr>
                        <td align="center">{index + 1}</td>
                        <td align="center">{results.name}</td>
                        <td align="center">{results.floor}</td>
                        <td align="center">{results.building}</td>
                        <td align="center">{results.workplace.map((results, index) => (
                            <tr>
                                <td align="center">{index + 1}. </td>
                                <td align="center">{results.name}</td>
                            </tr>
                        ))}
                        </td>
                        <td align="center">
                            <ModalWorkplace
                                create={false}
                                room={room}
                                resetState={props.resetState}
                                newWorkplace={props.newWorkplace}
                            />
                            &nbsp;&nbsp;
                            <RemoveWorkplace
                                id={room.id}
                                resetState={props.resetState}
                            />
                        </td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
    )
}

export default ListWorkplace