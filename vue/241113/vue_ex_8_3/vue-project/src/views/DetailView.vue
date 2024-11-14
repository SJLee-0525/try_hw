<template>
  <div>
    <h1>할 일 상세</h1>
    <div v-if="detailTodo">
      <p>할 일 번호 : {{ detailTodo.id }}</p>
      <p>할 일 제목 : {{ detailTodo.work }}</p>
      <p>할 일 내용 : {{ detailTodo.content }}</p>
      <p>할 일 상태 : {{ detailTodo.is_completed }}</p>
      <p>할 일 생성일 : {{ detailTodo.created_at }}</p>
    </div>
  </div>
</template>

<script setup>
import { useTodoStore } from '@/stores/todoStore';
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import axios from 'axios';


const store = useTodoStore()
const route = useRoute()

const detailTodo = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.BASE_URL}/api/v1/todos/${route.params.id}/`
  })
    .then((response) => {
      console.log(response)
      detailTodo.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>

<style scoped>

</style>