<template>
<main>
  <h1>할 일 목록</h1>
  <!-- {{ store.todos }} -->
  <TodoList
    :todos="store.todos"
  />
</main>
</template>

<script setup>
import { onMounted } from 'vue'
import { useTodoStore } from "@/stores/todoStore.js";
import TodoList from '@/components/TodoList.vue';

const store = useTodoStore()
onMounted(() => {
  store.getTodos()
})

</script>

<style>

</style>
