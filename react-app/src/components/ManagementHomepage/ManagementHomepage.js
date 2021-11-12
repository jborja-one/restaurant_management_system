import React from 'react';
import {
	autocompleteClasses,
	Container,
	Grid,
	Paper,
	Typography,
} from '@mui/material';
import './ManagementHomepage.css';
import { makeStyles } from '@material-ui/styles';

// const useStyles = makeStyles({
// 	paper: {
// 		margin: 20,
// 		height: 120,
// 		width: 120,
// 		textAlign: 'center',
// 		padding: 60,
// 		cursor: 'pointer',
// 		fontSize: 30,
// 		'&:hover': {
// 			margin: 10,
// 			height: 150,
// 			width: 150,
// 		},
// 	},
// 	container: {
// 		color: 'blue',
// 	},
// 	title: {
// 		display: 'flex',
// 		justifyContent: 'center',
// 		marginBottom: 50 | 50 | 'auto',
// 		textDecoration: 'underline',
// 		alignItems: 'center',
// 	},
// 	// grid: {
// 	// 	margin: 30,
// 	// },
// });

const ManagementHomepage = () => {
	// const classes = useStyles();

	return (
		<Container className='container '>
			<Container>
				<Typography variant='h3' className='title'>
					Main Menu
				</Typography>
			</Container>
			<Grid container spacing={4} className='grid'>
				<Paper className='paper' elevation={12}>
					Menu
				</Paper>
				<Paper className='paper' elevation={12}>
					Inventory
				</Paper>
				<Paper className='paper' elevation={12}>
					Reports
				</Paper>
				<Paper className='paper' elevation={12}>
					Test
				</Paper>
				<Paper className='paper' elevation={12}>
					Test
				</Paper>
				<Paper className='paper' elevation={12}>
					Test
				</Paper>
				<Paper className='paper' elevation={12}>
					Test
				</Paper>
				<Paper className='paper' elevation={12}>
					Test
				</Paper>
			</Grid>
		</Container>
	);
};

export default ManagementHomepage;
