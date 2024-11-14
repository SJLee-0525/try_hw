<template>
  <div>
    <h1>카테고리 생성 페이지</h1>
    <form @submit.prevent="createCategory">
      <label for="categoty_create">Category 종류: </label>
      <input type="text" id="category_create" v-model.trim="inputData">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { usePostsStore } from '@/stores/counter';
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const store = usePostsStore()
const route = useRoute()

const inputData = ref(null)

const createCategory = function () {
  axios({
    method: 'post',
    url: `${store.BASE_URL}/api/v1/category/`,
    data: {
      name: inputData.value
    }
  })
    .then((response) => {
      console.log(response)
      route.push({ name: 'home' })
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>

<style scoped>

</style>