<template>
  <div>
    <h1>User Profile</h1>
    <h3>Username: {{ username }}</h3>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref } from 'vue'

const route = useRoute()
const username = ref(route.params.username)
</script>

<style scoped>

</style>