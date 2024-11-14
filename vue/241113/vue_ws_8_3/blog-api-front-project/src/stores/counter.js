import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const usePostsStore = defineStore('posts', () => {
  const BASE_URL = 'http://127.0.0.1:8000'
  const posts = ref(null)

  const getPostsList = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/posts/`
    })
      .then((response) => {
        console.log(response.data)
        posts.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return { posts, BASE_URL, getPostsList }
})
