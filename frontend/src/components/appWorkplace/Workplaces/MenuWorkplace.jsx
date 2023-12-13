import {IconButton, Menu, MenuItem} from "@mui/material";
import ModalWorkplace from "./ModalWorkplace";
import RemoveWorkplace from "./RemoveWorkplace";
import * as React from "react";
import MoreVertIcon from "@mui/icons-material/MoreVert";


const MenuWorkplace = (props) => {
    const {room} = props
    const [anchorElMenu, setAnchorElMenu] = React.useState(null);
    const openMenu = Boolean(anchorElMenu);
    const handleClickMenu = (event) => {
        setAnchorElMenu(event.currentTarget);
    };
    const handleCloseMenu = () => {
        setAnchorElMenu(null);
    };
    return (
        <div>
            <IconButton
                aria-label="more"
                id="long-button"
                aria-controls={openMenu ? 'long-menu' : undefined}
                aria-expanded={openMenu ? 'true' : undefined}
                aria-haspopup="true"
                onClick={handleClickMenu}
            >
                <MoreVertIcon/>
            </IconButton>
            <Menu
                id="long-menu"
                MenuListProps={{
                    'aria-labelledby': 'long-button',
                }}
                anchorEl={anchorElMenu}
                open={openMenu}
                onClose={handleCloseMenu}
            >
                <MenuItem onClick={handleCloseMenu}>
                    <ModalWorkplace
                        create={true}
                        resetState={props.resetState}
                        newWorkplace={true}
                    />
                </MenuItem>
                <MenuItem onClick={handleCloseMenu}>
                    <ModalWorkplace
                        create={false}
                        room={room}
                        resetState={props.resetState}
                        newWorkplace={props.newWorkplace}
                    />
                </MenuItem>
                <MenuItem onClick={handleCloseMenu}>
                    <RemoveWorkplace
                        id={room.id}
                        resetState={props.resetState}
                    />
                </MenuItem>
            </Menu>
        </div>
    )
};

export default MenuWorkplace