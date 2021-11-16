import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getMenuItems } from '../../store/menu_items';

const MenuItems = () => {
	const menu_items = Object.values(useSelector((state) => state.menu_items));
	const dispatch = useDispatch();

	console.log('------------------------------------');
	console.log(menu_items, 'from component');
	console.log('------------------------------------');
	useEffect(() => {
		dispatch(getMenuItems());
	}, [dispatch]);
	return (
		<>
			<div>
				<h1>Menu</h1>
			</div>
			<div>
				{menu_items.map((item) => {
					return <div>{item.item_name}</div>;
				})}
			</div>
		</>
	);
};

export default MenuItems;
