<template>
  <div>
    <nav>
      <RouterLink :to="{ name: 'MainView' }">HOME</RouterLink> | 
      <RouterLink :to="{ name: 'PostListView' }">POSTLIST</RouterLink> | 
      <RouterLink :to="{ name: 'CreateCategoryView' }">CREATE CATEGORY</RouterLink>
    </nav>
  </div>
  <RouterView />
</template>

<script setup>
import MainView from './views/MainView.vue';
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
</style>
