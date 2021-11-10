import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
// import { makeStyles } from '@mui/styles';
import { makeStyles } from '@material-ui/styles';

const useStyles = makeStyles({
	field: {
		marginBottom: 20,
		marginTop: 20,
		width: 350,
	},
	loginTitle: {
		display: 'flex',
		justifyContent: 'center',
		marginBottom: 20,
		marginTop: 40,
	},
	container: {
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
		margin: 50,
	},
});

const LoginForm = () => {
	const [errors, setErrors] = useState([]);
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const user = useSelector((state) => state.session.user);
	const dispatch = useDispatch();

	const classes = useStyles();

	const onLogin = async (e) => {
		e.preventDefault();
		const data = await dispatch(login(email, password));
		if (data) {
			setErrors(data);
		}
	};

	const updateEmail = (e) => {
		setEmail(e.target.value);
	};

	const updatePassword = (e) => {
		setPassword(e.target.value);
	};

	if (user) {
		return <Redirect to='/' />;
	}

	return (
		<Container className={classes.container} component='div'>
			<Typography
				className={classes.loginTitle}
				variant='h4'
				component='h2'
				color='primary'>
				Restaurant Management System
			</Typography>
			<form onSubmit={onLogin} noValidate>
				<div>
					{errors.map((error, ind) => (
						<div key={ind}>{error}</div>
					))}
				</div>
				<TextField
					className={classes.field}
					onChange={updateEmail}
					label='Email'
					variant='outlined'
					value={email}
					color='secondary'
					required
				/>
				<br />
				<TextField
					className={classes.field}
					onChange={updatePassword}
					label='Password'
					variant='outlined'
					value={password}
					type='password'
					color='secondary'
					required
				/>
				<br />
				<Button
					type='submit'
					variant='contained'
					color='primary'
					className={classes.button}
					margin='normal'>
					Login
				</Button>
			</form>
		</Container>
	);
};

export default LoginForm;
