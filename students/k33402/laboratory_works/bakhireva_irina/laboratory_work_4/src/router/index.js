import {createRouter, createWebHistory} from 'vue-router'
import LoginView from "@/views/LoginView.vue";
import HomeView from "@/views/HomeView.vue";
import RegisterView from "@/views/RegisterView.vue";
import Applicant from "@/views/Applicant.vue";
import MyCV from "@/views/applicant/MyCV.vue";
import AvailableCourses from "@/views/applicant/AvailableCourses.vue";
import VacanciesForMe from "@/views/applicant/VacanciesForMe.vue";
import Companies from "@/views/applicant/Companies.vue";
import Profile from "@/views/common/Profile.vue";
import EditProfile from "@/views/common/EditProfile.vue";
import Logout from "@/views/common/Logout.vue";
import Company from "@/views/applicant/Company.vue";
import MyCompany from "@/views/hr/MyCompany.vue";
import HR from "@/views/HR.vue";
import CreateVacancy from "@/views/hr/CreateVacancy.vue";
import AllCV from "@/views/hr/AllCV.vue";
import CV from "@/views/hr/CV.vue";
import CVForVacancy from "@/views/hr/CVForVacancy.vue";
import EditVacancy from "@/views/hr/EditVacancy.vue";

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: "/login",
			component: LoginView,
			name: "Login"
		},
		{
			path: "/register",
			component: RegisterView,
			name: "Register"
		},
		{
			path: "/",
			component: HomeView,
			name: "Home"
		},
		{
			path: "/hr",
			component: HR,
			name: "HR",
			children: [
				{
					path: "company",
					component: MyCompany,
					name: "MyCompany",
				},
				{
					path: "create-vacancy",
					component: CreateVacancy,
					name: "CreateVacancy",
				},
				{
					path: "cvs",
					component: AllCV,
					name: "AllCV",
				},
				{
					path: "cv/:id",
					component: CV,
					name: "CV",
				},
				{
					path: "vacancy-cv/:id",
					component: CVForVacancy,
					name: "CVForVacancy",
				},
				{
					path: "vacancy-edit/:id",
					component: EditVacancy,
					name: "EditVacancy",
				}
			]
		},
		{
			path: "/applicant",
			component: Applicant,
			name: "Applicant",
			children: [
				{
					path: "cv",
					component: MyCV,
					name: "MyCV",
				},
				{
					path: "available-courses",
					component: AvailableCourses,
					name: "AvailableCourses",
				},
				{
					path: "my-vacancys",
					component: VacanciesForMe,
					name: "VacanciesForMe",
				},
				{
					path: "companies",
					component: Companies,
					name: "Companies",
				},
				{
					path: "company/:id",
					component: Company,
					name: "Company"
				}
			]
		},
		{
			path: "/profile",
			component: Profile,
			name: "Profile"
		},
		{
			path: "/edit-profile",
			component: EditProfile,
			name: "EditProfile"
		},
		{
			path: "/profile",
			component: Logout,
			name: "Logout"
		},
		{
			path: "/",
			component: HomeView,
			name: "Home"
		}
	]
})

export default router
