<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <p>{{ store.posts }}</p>
  </div>
</template>

<script setup>
import { usePostsStore } from '@/stores/counter';
import { onMounted } from 'vue';

const store = usePostsStore()

onMounted(() => {
  store.getPostsList()
})
</script>

<style scoped>

</style>