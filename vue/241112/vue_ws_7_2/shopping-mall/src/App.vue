<template>
  <nav>
    <RouterLink :to="{ 'name': 'home' }"><a>HOME</a></RouterLink>
    <RouterLink :to="{ 'name': 'products' }">PRODUCTS</RouterLink>
    <RouterLink :to="{ 'name': 'favorite' }">FAVORITE</RouterLink>
  </nav>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-evenly;
  background-color: rgb(41, 41, 41);
  padding: 15px;
}

nav > a {
  color: white;
}
</style>
