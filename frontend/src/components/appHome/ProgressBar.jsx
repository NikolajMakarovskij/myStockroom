import * as React from 'react';
import PropTypes from "prop-types";
import {LinearProgress, Typography, Box, linearProgressClasses, styled} from "@mui/material";


const BorderLinearProgress = styled(LinearProgress)(({theme}) => ({
    height: 10,
    borderRadius: 5,
    [`&.${linearProgressClasses.colorPrimary}`]: {
        backgroundColor: theme.palette.grey[theme.palette.mode === 'light' ? 25 : 100],
    },
    [`&.${linearProgressClasses.bar}`]: {
        borderRadius: 5,
        backgroundColor: theme.palette.mode === 'light' ? '#1a90ff' : '#308fe8'
    }
}));

function LinearProgressWithLabel(props) {
    return(
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
            <Box sx={{ width: '100%', mr: 1 }}>
                <BorderLinearProgress variant='determinate' {...props}/>
            </Box>
            <Box>
                <Typography variant='body2' color='text.secondary'>
                    {`${Math.round(
                        props.value,
                    )}%`}
                </Typography>
            </Box>
        </Box>
    );
}

LinearProgressWithLabel.prototype = {
    value: PropTypes.number.isRequired,
};

/*
export default function LinearWithValueLabel() {
    const [progress, setProgress] = React.useState(10)

    React.useEffect(() => {
        const timer = setInterval(() => {
            setProgress((prevProgress) => (prevProgress >= 100 ? 10 : prevProgress + 10));
            }, 10);
            return () => {
                clearInterval(timer);
            };
        }, []);

    return (
        <Box sx={{width: '100%'}}>
            <LinearProgressWithLabel value={progress} />
        </Box>
    );
}
 */

export default function LinearIndeterminate() {
  return (
    <Box sx={{ width: '100%' }}>
      <LinearProgress />
    </Box>
  );
}