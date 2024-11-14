<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <div>
      <form @click.prevent="createArticle()">
        <div>
          <label for="title">제목 : </label>
          <input type="text" id="title" v-model.trim="title">
        </div>
        <div>
          <label for="content">내용 : </label>
          <input type="text" id="content" v-model.trim="content">
        </div>
        <input type="submit">
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const title = ref(null)
const content = ref(null)

const createArticle = function () {
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/api/v1/articles/',
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then((response) => {
      console.log(response.data)
      router.push({ name: 'home' })
    })
    .catch((error) => {
      console.log(error)
    })
}


</script>

<style scoped>

</style>