import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const router = useRouter()

  const articles = ref([])
  const token = ref(null)

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((response) => {
        console.log(response)
        articles.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username,
        password1,
        password2
      }
    })
      .then((response) => {
        console.log('가입 성공')
        console.log(response.data)
        const password = password1
        signIn({ username, password })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const signIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username,
        password,
      }
    })
      .then((response) => {
        console.log('로그인 성공')
        console.log(response)
        token.value = response.data.key
        router.push({ name: 'home' })
      })
      .catch((error) => {
        console.log(error)
      })
    }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  
  return { articles, token, isLogin, getArticles, createArticle, signUp, signIn }
})
