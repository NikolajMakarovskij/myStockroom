import {React, useState} from 'react'
import PropTypes from 'prop-types';
import {Box, Tabs, Tab, Typography, createTheme, ThemeProvider, AppBar} from '@mui/material';
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

export default function MaterialReactTableTabsList({columns, data, category, renderRowActionMenuItems, renderDetailPanel, ...props}) {
    const [slug, setSlug] = useState(category ? category.slug : '')
    const [value, setValue] = useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    return(
        <>
            <ThemeProvider theme={darkTheme}>
                <Box sx={{ bgcolor: 'background.paper',  borderRadius: '3px'}}>
                    <AppBar position="static" sx={{borderRadius: '3px'}}>
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
                    enableExpandAll={false} //disable expand all button
                    muiDetailPanelProps={() => ({
                        sx: (theme) => ({
                            backgroundColor:
                                theme.palette.mode === 'dark'
                                    ? 'rgba(255,210,244,0.1)'
                                        : 'rgba(0,0,0,0.1)',
                        }),
                    })}
                    muiExpandButtonProps={({ row, table }) => ({
                        onClick: () => table.setExpanded({ [row.id]: !row.getIsExpanded() }), //only 1 detail panel open at a time
                        sx: {
                            transform: row.getIsExpanded() ? 'rotate(180deg)' : 'rotate(-90deg)',
                            transition: 'transform 0.2s',
                        },
                    })}
                    renderDetailPanel={renderDetailPanel}
                />
            </CustomTabPanel>
            {category.map((cat, index) => (
                <CustomTabPanel value={value} index={index+1}>
                    <MaterialReactTableList
                        columns={columns}
                        data={data.filter(item => item.categories ? item.categories.slug.includes(cat.slug) : false)}
                        renderRowActionMenuItems={renderRowActionMenuItems}
                                            enableExpandAll={false} //disable expand all button
                    muiDetailPanelProps={() => ({
                        sx: (theme) => ({
                            backgroundColor:
                                theme.palette.mode === 'dark'
                                    ? 'rgba(255,210,244,0.1)'
                                        : 'rgba(0,0,0,0.1)',
                        }),
                    })}
                    muiExpandButtonProps={({ row, table }) => ({
                        onClick: () => table.setExpanded({ [row.id]: !row.getIsExpanded() }), //only 1 detail panel open at a time
                        sx: {
                            transform: row.getIsExpanded() ? 'rotate(180deg)' : 'rotate(-90deg)',
                            transition: 'transform 0.2s',
                        },
                    })}
                    renderDetailPanel={renderDetailPanel}
                    />
                </CustomTabPanel>
            ))}
        </>
    )
};