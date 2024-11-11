import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '@/views/UserView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
    {
      path: '/user/:username',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from) => {
        if (to.params.username !== 'admin') {
          console.log(to)
          const answer = window.alert('admin이 아닙니다.')
          return { name: 'home' }
        }
      }
    },
  ]
})

export default router
