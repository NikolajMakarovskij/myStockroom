import React  from 'react';
import {Table} from "reactstrap";
import ModalWorkplace from "./ModalWorkplace";
import RemoveWorkplace from "./RemoveWorkplace";

const ListWorkplaces = (props) => {
    const {room} = props
    return (
        <Table dark>
            <thead align="center">
            <tr>
                <th>Кабинет</th>
                <th>Этаж</th>
                <th>Здание</th>
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
                        <td>{results[index].name}</td>
                        <td>{results[index].floor}</td>
                        <td>{results[index].building}</td>
                        <td>
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

export default ListWorkplaces