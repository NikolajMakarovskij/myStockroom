import {React, useState} from 'react'
import PropTypes from 'prop-types';
import {Link} from "react-router-dom";
import {IconButton, MenuItem, Box, Tabs, Tab, Typography, createTheme, ThemeProvider, AppBar} from '@mui/material';
import MaterialReactTableList from "./MaterialReactTableList";

const darkTheme = createTheme({
  palette: {
      mode: 'dark',
  },
});

function CustomTabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

CustomTabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

export default function MaterialReactTableTabsList({columns, data, category, renderRowActionMenuItems, ...props}) {
    const [slug, setSlug] = useState(category ? category.slug : '')
    const [value, setValue] = useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    return(
        <>
            <ThemeProvider theme={darkTheme}>
                <Box sx={{ bgcolor: 'background.paper' }}>
                    <AppBar position="static">
                        <Tabs
                            value={value}
                            onChange={handleChange}
                            aria-label="basic tabs example"
                        >
                            <Tab label="Все"  {...a11yProps(0)}/>
                            {category.map((cat, index) => (
                                <Tab label={cat.name} {...a11yProps(index+1)} />
                            ))}
                        </Tabs>
                    </AppBar>
                </Box>
            </ThemeProvider>
            <CustomTabPanel value={value} index={0}>
                <MaterialReactTableList
                    columns={columns}
                    data={data}
                    renderRowActionMenuItems={renderRowActionMenuItems}
                />
            </CustomTabPanel>
            {category.map((cat, index) => (
                <CustomTabPanel value={value} index={index+1}>
                    <MaterialReactTableList
                        columns={columns}
                        data={data.filter(item => item.categories ? item.categories.slug.includes(cat.slug) : false)}
                        renderRowActionMenuItems={renderRowActionMenuItems}
                    />
                </CustomTabPanel>
            ))}
        </>
    )
};