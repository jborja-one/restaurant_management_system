const LOAD_MENU = 'menu_items/LOAD_MENU';

const load_menu = (menu_items) => ({
	type: LOAD_MENU,
	menu_items,
});

export const getMenuItems = () => async (dispatch) => {
	const res = await fetch('/api/menu_items/');
	console.log(res, 'from store');
	debugger;
	if (res.ok) {
		const menu = await res.json();
		dispatch(load_menu(menu));
		debugger;
		return res;
	}
};

const menuItemsReducer = (state = {}, action) => {
	if (!action) return state;

	switch (action.type) {
		case LOAD_MENU: {
			const { menu_items } = action.menu_items;
			debugger;
			console.log('------------------------------------');
			console.log(menu_items, 'from reducer');
			console.log('------------------------------------');
			return { ...menu_items };
		}
		default:
			return state;
	}
};

export default menuItemsReducer;
