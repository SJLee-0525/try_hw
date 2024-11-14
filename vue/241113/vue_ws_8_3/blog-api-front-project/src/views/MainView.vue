<template>
  <div>
    <div>
      <h1>성준이의 블로그</h1>
      <div v-if="categories">
        <h3>카테고리 목록</h3>
        <ul v-for="category in categories">
          <li>{{ category.name }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { usePostsStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted } from 'vue';
import { ref } from 'vue';

const store = usePostsStore()

const categories = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.BASE_URL}/api/v1/category/`,
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