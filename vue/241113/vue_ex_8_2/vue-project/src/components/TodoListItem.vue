<template>
  <div>
    <h3>{{ todo.id }}번째 할 일</h3>
    <p><strong>{{ todo.work }}</strong></p>
    <p>{{ todo.content }}</p>
    <p>{{ todo.is_completed }}</p>
    <p>{{ todo.created_at }}</p>
    <hr>
  </div>
</template>

<script setup>
// import { useTodoStore } from '@/stores/todoStore';
// import axios from 'axios';

defineProps({
  todo: Object,
})

// const store = useTodoStore()

// const fetch_todo = function () {
//   axios({
//     method: 'get',
//     url: `${store.BASE_URL}/api/v1/todos/${todo.id}`
//   })
//     .then((response) => {
//       console.log(response.data)
//     })
//     .catch((error) => {
//       console.log(error)
//     })
// }
</script>

<style scoped>

</style>