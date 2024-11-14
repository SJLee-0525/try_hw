<template>
  <div v-for="todo in todos" :key="todo.id">
    <TodoListItem :todo="todo"/>
  </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue';

defineProps({
  todos: Array
})
</script>

<style scoped>

</style>