import {createRouter, createWebHistory} from "vue-router";
import Staff from "@/views/Staff.vue";
import SignIn from "@/views/SignIn.vue";
import SignUp from "@/views/SignUp.vue";
import Products from "@/views/Products.vue";
import Sales from "@/views/Sales.vue";
import Profile from "@/views/Profile.vue";
import EditProfile from "@/views/EditProfile.vue";
import Logout from "@/views/Logout.vue";

const routes = [
	{
		path: "/signin",
		component: SignIn,
		name: "SignIn"
	},
	{
		path: "/signup",
		component: SignUp,
		name: "SignUp"
	},
	{
		path: "/",
		component: Staff,
		name: "Staff"
	},
	{
		path: "/products",
		component: Products,
		name: "Products"
	},
	{
		path: "/sales",
		component: Sales,
		name: "Sales"
	},
	{
		path: "/profile",
		component: Profile,
		name: "Profile",
	},
	{
		path: "/edit-profile",
		component: EditProfile,
		name: "EditProfile"
	},
	{
		path: "/logout",
		component: Logout,
		name: "Logout"
	},
];

export default createRouter({
	history: createWebHistory(), routes
})
