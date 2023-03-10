import { createRouter, createWebHistory } from 'vue-router'
import Auth from './views/Auth.vue'
import AllUsers from '@/views/AllUsers.vue'
import UserDetail from '@/views/User.vue'
import NewReader from '@/views/NewReader.vue';
import LibrarianList from '@/views/LibrarianList.vue'
import AddLibrarian from '@/views/CreateLibrarian.vue'




const routes = [
    // { path: '/', component: Home },
    { path: '/login', component: Auth },
    {
        path: '/users',
        name: 'AllUsers',
        component: AllUsers
    },
    {
        path: '/users/:id',
        name: 'UserDetail',
        component: UserDetail,
        props: true
    },
    {
        path: '/new-reader',
        name: 'NewReader',
        component: NewReader,
    },
    {
        path: '/librarians',
        name: 'LibrarianList',
        component: LibrarianList
    },
    {
        path: '/add-librarian',
        name: 'AddLibrarian',
        component: AddLibrarian
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
