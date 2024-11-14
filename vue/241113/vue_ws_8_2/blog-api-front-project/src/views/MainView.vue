<template>
  <div>
    <nav>
      <RouterLink :to="{ name: 'MainView' }">HOME</RouterLink>
    </nav>
    <div>
      <h1>성준이의 블로그</h1>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>

</style>