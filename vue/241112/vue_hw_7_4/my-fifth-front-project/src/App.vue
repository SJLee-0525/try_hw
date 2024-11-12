<template>
  <div>
    <RouterLink :to="{ name: 'main'}">MAIN</RouterLink>
    <h1>pinia + router 연습하기</h1>

    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
</style>
