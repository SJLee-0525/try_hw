<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home' }">HOME</RouterLink> | 
      <RouterLink :to="{ name: 'about' }">ABOUT</RouterLink>

      <RouterView />
    </nav>
  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
