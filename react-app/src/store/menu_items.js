const LOAD_MENU = 'menu_items/LOAD_MENU';

const load_menu = (menu_items) => ({
	type: LOAD_MENU,
	menu_items,
});

export const getMenuItems = () => async (dispatch) => {
	const res = await fetch('/api/menu_items/');

	if (res.ok) {
		const menu = await res.json();
		dispatch(load_menu(menu.menu_items));
		return res;
	}
};

const menuItemsReducer = (state = {}, action) => {
	if (!action) return state;
	switch (action.type) {
		case LOAD_MENU: {
			const newState = {};
			action.menu_items.forEach((item) => {
				newState[item.id] = item;
			});
			return newState;
		}
		default:
			return state;
	}
};

export default menuItemsReducer;
