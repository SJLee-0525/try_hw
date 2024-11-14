import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignInView from '../views/SignInView.vue'
import SignUpView from '../views/SignUpView.vue'
import { useArticleStore } from '../stores/articles'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignInView
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useArticleStore()

  if ((to.name === 'home' || to.name === 'create') && !store.isLogin) {
    window.alert('로그인이 필요합니다!')
    return { name: 'LogInView' }
  }
  if ((to.name === 'signup' || to.name === 'signin') && store.isLogin) {
    window.alert(`이미 로그인이 되어있습니다!`)
    return { name: 'ArticleView' }
  }
})

export default router
