<template>
  <div>
    <h2>상세 프로필</h2>
    <p>반갑습니다. {{ userName }}입니다.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userName = ref(route.params.username)
</script>

<style scoped>
</style>