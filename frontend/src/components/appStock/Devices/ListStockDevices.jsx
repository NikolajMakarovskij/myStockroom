import {React, useMemo, useState, useCallback, useEffect,} from 'react'
import PropTypes from 'prop-types';
import {
    MaterialReactTable,
} from 'material-react-table';
//import {createTheme} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {Link} from "react-router-dom";
import {IconButton, MenuItem, Box, Tabs, Tab} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import {MRT_Localization_RU} from 'material-react-table/locales/ru';
import LinearIndeterminate from "../../appHome/ProgressBar.jsx";
import MaterialReactTableList from "../../Tables/MaterialReactTableList";


function samePageLinkNavigation(event) {
  if (
    event.defaultPrevented ||
    event.button !== 0 || // ignore everything but left-click
    event.metaKey ||
    event.ctrlKey ||
    event.altKey ||
    event.shiftKey
  ) {
    return false;
  }
  return true;
}

function LinkTab(props) {
  return (
    <Tab
      component="a"
      onClick={(event) => {
        if (samePageLinkNavigation(event)) {
          event.preventDefault();
        }
      }}
      aria-current={props.selected && 'page'}
      {...props}
    />
  );
}

LinkTab.propTypes = {
  selected: PropTypes.bool,
};
export default function ListStockDevices() {
    const [value, setValue] = useState(0);
    const [device, setDevices] = useState()
    const [category, setCategory] = useState('')
    const [slug, setSlug] = useState(category ? category.slug : '')
    const [loading, setLoading] = useState(true)

    const GetData = useCallback(async () => {
        await AxiosInstanse.get(`stockroom/api/v1/stock_dev_list/`, {timeout: 1000*30}).then((res) => {
            setDevices(res.data)
            setLoading(false)
        })
        // await AxiosInstanse.get(`stockroom/api/v1/stock_dev_cat/`).then((res) => {
        //     setCategory(res.data)
        //     setLoading(false)
        // })

    })

    useEffect(() =>{
        GetData();
    },[])

  const handleChange = (event, newValue) => {
    if (
        event.type !== 'click' ||
        (event.type === 'click' && samePageLinkNavigation(event))
    ) {
        setValue(newValue);
    }
  };
    const columns = useMemo(() => [
        {
            id: 'stock_model',
            accessorKey: 'stock_model.name',
            header: 'Устройство',
        },
                {
            accessorKey: 'stock_model.description',
            header: 'Описание',
        },
                {
            accessorKey: 'stock_model.note',
            header: 'Примечание',
        },
                {
            accessorKey: 'stock_model.quantity',
            header: 'Количество',
        },
        {
            accessorKey: 'stock_model.serial',
            header: 'Серийный №',
        },
        {
            accessorKey: 'stock_model.invent',
            header: 'Инвентарный №',
        },
        {
            accessorKey: 'rack',
            header: 'Стеллаж',
        },
            {
            accessorKey: 'shelf',
            header: 'Полка',
        },
        {
            accessorKey: 'stock_model.workplace.name',
            header: 'Рабочее место',
        },
        {
            accessorKey: 'stock_model.workplace.room.building',
            header: 'Здание',
        }, {
            accessorKey: 'categories.name',
            header: 'Группа',
        },
        {
            accessorKey: 'dateAddToStock',
            header: 'Приход',
        },
        {
            accessorKey: 'dateInstall',
            header: 'Установка',
        }
    ],
        [],
    );

    return(
        <>
            {loading ? <LinearIndeterminate/> :
                (
                    <>
                        {/*<Tabs
                            value={value}
                            onChange={handleChange}
                            aria-label="nav tabs example"
                            role="navigation"
                        >
                            <LinkTab label="Все" href="/stock/device/list" />
                            {category.map((cat, index) => (
                                <LinkTab label={cat.name} href={cat.slug} key={index} />
                            ))}
                        </Tabs>*/}
                        <MaterialReactTableList
                            columns={columns}
                            data={device}
                            renderRowActionMenuItems={({
                                row,
                                menuActions = [
                                    //{'name': 'Добавить', 'path': `create`, 'icon': <AddIcon/>, 'color': 'success',},
                                    //{'name': 'Редактировать', 'path': `edit/${row.original.id}`, 'icon': <EditIcon/>, 'color': 'primary',},
                                    //{'name': 'Удалить', 'path': `remove/${row.original.id}`, 'icon': <DeleteIcon/>, 'color': 'error',},
                                ], }) => [
                                menuActions.map(
                                (item, index) => (
                                    <MenuItem key={index} component={Link} to={item.path}>
                                    <IconButton color={item.color} >
                                        {item.icon}
                                    </IconButton>
                                    {item.name}
                                </MenuItem>
                                ))
                            ]}
                        />
                    </>
                )
            }
        </>
    )
};