<template>
  <div>
    <p>번호: {{ targetPost.id }}</p>
    <p>제목: {{ targetPost.title }}</p>
    <p>내용: {{ targetPost.content}}</p>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const userName = ref(route.params.username)
const posts = ref([
  { id: 1 , title: 'Post 1' , content: 'Content 1' },
  { id: 2 , title: 'Post 2' , content: 'Content 2' },
  { id: 3 , title: 'Post 3' , content: 'Content 3' },
])
const postId = computed(() => route.params.id)

const targetPost = computed(() => {
  console.log(posts)
  return posts.value.find(post => post.id === Number(postId.value))
})

watch(postId, (newId) => {
  console.log(newId)
})
</script>

<style scoped>

</style>