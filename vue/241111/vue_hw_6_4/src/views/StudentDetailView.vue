<template>
  <div>
    <h1>학생 상세 정보 페이지입니다.</h1>
    <p>이름: {{ studentName }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const studentName = ref(route.params.name)
</script>

<style scoped>

</style>