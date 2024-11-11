<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home' }">HOME</RouterLink> | 
      <RouterLink :to="{ name: 'about' }">ABOUT</RouterLink> | 
      <RouterLink :to="{ name: 'user', params: { 'username': userName } }">USER</RouterLink>
      <RouterView />
    </nav>
  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'

const userName = ref('admin')
</script>

<style scoped>
</style>
