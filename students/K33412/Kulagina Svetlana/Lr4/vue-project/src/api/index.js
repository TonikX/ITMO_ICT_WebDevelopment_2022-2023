import instance from "@/api/instance"
import CardApi from "@/api/cards"
import LoginApi from '@/api/login';
import RegisterApi from '@/api/register';
import UserEventsApi from '@/api/userEvents';
import CalendarEventsApi from "./calendarEvents";
 
const cardApi = new CardApi(instance);
const loginApi = new LoginApi(instance);
const registerApi = new RegisterApi(instance)
const userEventsApi = new UserEventsApi(instance)
const calendarEventsApi = new CalendarEventsApi(instance)

export {
 cardApi,
 loginApi,
 registerApi,
 userEventsApi,
 calendarEventsApi
}
