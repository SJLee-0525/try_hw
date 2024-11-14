<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <RouterLink :to="{ name: 'CreatePostView' }">게시글 생성</RouterLink>
    <p>{{ store.posts }}</p>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { usePostsStore } from '@/stores/counter';
import { onMounted } from 'vue';

const store = usePostsStore()

onMounted(() => {
  store.getPostsList()
})
</script>

<style scoped>

</style>