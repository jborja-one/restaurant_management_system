import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import ManagementHomepage from './components/ManagementHomepage/ManagementHomepage';
import { authenticate } from './store/session';
import MenuItems from './components/MenuItems/MenuItems';

function App() {
	const [loaded, setLoaded] = useState(false);
	const dispatch = useDispatch();

	useEffect(() => {
		(async () => {
			await dispatch(authenticate());
			setLoaded(true);
		})();
	}, [dispatch]);

	if (!loaded) {
		return null;
	}

	return (
		<BrowserRouter>
			<NavBar />
			<Switch>
				<Route path='/login' exact={true}>
					<LoginForm />
				</Route>
				<Route path='/sign-up' exact={true}>
					<SignUpForm />
				</Route>
				<ProtectedRoute path='/users' exact={true}>
					<UsersList />
				</ProtectedRoute>
				<ProtectedRoute path='/users/:userId' exact={true}>
					<User />
				</ProtectedRoute>
				<ProtectedRoute path='/' exact={true}>
					<ManagementHomepage />
				</ProtectedRoute>
				<ProtectedRoute path='/menu' exact={true}>
					<MenuItems />
				</ProtectedRoute>
			</Switch>
		</BrowserRouter>
	);
}

export default App;
