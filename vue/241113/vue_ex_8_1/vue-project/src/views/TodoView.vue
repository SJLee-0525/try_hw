<template>
  <main>
    <h1>할 일 목록</h1>
  </main>
  <p>{{ store.todos }}</p>
</template>

<script setup>
import { ref } from 'vue';
import { useTodoStore } from '@/stores/todoStore';
import { onMounted } from 'vue';

const store = useTodoStore()

onMounted(() => {
  store.getTodos()
})
</script>

<style>

</style>
