import React from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';

const NavBar = () => {
	const sessionUser = useSelector((state) => state.session.user);

	let sessionLinks;
	if (!sessionUser) {
		return null;
	} else {
		sessionLinks = (
			<nav>
				<ul>
					<li>
						<NavLink to='/' exact={true} activeClassName='active'>
							Home
						</NavLink>
					</li>
					{/* <li>
						<NavLink
							to='/login'
							exact={true}
							activeClassName='active'>
							Login
						</NavLink>
					</li>
					<li>
						<NavLink
							to='/sign-up'
							exact={true}
							activeClassName='active'>
							Sign Up
						</NavLink>
					</li> */}
					<li>
						<NavLink
							to='/users'
							exact={true}
							activeClassName='active'>
							Users
						</NavLink>
					</li>
					<li>
						<LogoutButton />
					</li>
				</ul>
			</nav>
		);
	}
	return sessionLinks;
};

export default NavBar;
