import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import PostListView from '@/views/PostListView.vue'
import CreateCategoryView from '@/views/CreateCategoryView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView,
    },
    {
      path: '/posts',
      name: 'PostListView',
      component: PostListView,
    },
    {
      path: '/category',
      name: 'CreateCategoryView',
      component: CreateCategoryView,
    },
  ],
})

export default router
