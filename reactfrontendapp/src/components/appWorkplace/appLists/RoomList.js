import {Table} from "reactstrap";
import ModalRooms from "../appModals/RoomModal";
import AppRemoveRoom from "../appRemoves/RoomRemove";
import React from "react";


const ListRooms = (props) => {
    const {rooms} = props
    return (
        <Table dark>
            <thead>
            <tr>
                <th>Кабинет</th>
                <th>Этаж</th>
                <th>Здание</th>
            </tr>
            </thead>
            <tbody>
            {!rooms || rooms.length <= 0 ? (
                <tr>
                    <td colSpan="6" align="center">
                        <b>Пока ничего нет</b>
                    </td>
                </tr>
            ) : rooms.map(rooms => (
                    <tr key={rooms.pk}>
                        <td>{rooms.name}</td>
                        <td>{rooms.floor}</td>
                        <td>{rooms.building}</td>
                        <td>
                            <ModalRooms
                                create={false}
                                room={rooms}
                                resetState={props.resetState}
                                newRoom={props.newRoom}
                            />
                            &nbsp;&nbsp;
                            <AppRemoveRoom
                                pk={rooms.pk}
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

export default ListRooms