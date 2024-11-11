<template>
  <MainPage />

  <RouterLink :to="{ name: 'some' }">SOME</RouterLink> | 
  <RouterLink :to="{ name: 'other' }">OTHER</RouterLink> | 
  <RouterLink :to="{ name: 'students' }">Students</RouterLink>
  <hr>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

import MainPage from '@/components/MainPage.vue';


</script>

<style scoped>
</style>
