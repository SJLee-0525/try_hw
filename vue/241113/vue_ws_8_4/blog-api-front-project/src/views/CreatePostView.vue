<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <div v-if="categories">
      <form @submit.prevent="createCategory">
      <select name="" id="" v-for="category in categories">
        <option value="">{{ category.name }}</option>
      </select>
      <div>
        <label for="post_create">제목: </label>
        <input type="text" id="post_title" v-model.trim="inputTitle">
      </div>
      <div>
        <label for="post_create">내용: </label>
        <input type="text" id="post_content" v-model.trim="inputContent">
      </div>
      <input type="submit">
    </form>
    </div>
  </div>
</template>

<script setup>
import { usePostsStore } from '@/stores/counter';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';



const store = usePostsStore()
const router = useRouter()

const inputTitle = ref(null)
const inputContent = ref(null)

const createPost = function () {
  axios({
    method: 'post',
    url: `${store.BASE_URL}/api/v1/posts/post/`,
    data: {
      title: inputTitle.value,
      content: inputContent.value,
    }
  })
    .then((response) => {
      console.log(response)
      router.push({ name: 'MainView' })
    })
    .catch((error) => {
      console.log(error)
    })
}

const categories = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.BASE_URL}/api/v1/posts/category/`,
  })
    .then((response) => {
      console.log(response.data)
      categories.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>

<style scoped>

</style>