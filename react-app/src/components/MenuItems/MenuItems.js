import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getMenuItems } from '../../store/menu_items';

const MenuItems = () => {
	const menu_items = Object.values(useSelector((state) => state.menu_items));
	const dispatch = useDispatch();
	// debugger;
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
					return (
						<div>
							{/* {console.log(
								item?.category.category_name,
								'from return'
							)} */}
							<div>{item.item_name}</div>
							<div>{item.item_price}</div>
							<div>{item.item_cost}</div>
							<div>
								{item?.ingredients !== undefined &&
									item?.category.category_name}
							</div>
						</div>
					);
				})}
			</div>
		</>
	);
};

export default MenuItems;
