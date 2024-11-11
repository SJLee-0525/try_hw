<template>
  <div>
    <h2>{{ userName}}이 작성한 게시글 </h2>
    <template v-for="(post, index) in posts" :key="post.id">
      <p>
        {{ index + 1 }}. <a href="#" @click="getPostDetail(post.id)">제목: {{ post.title }}</a>
      </p>
    </template>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, RouterLink, RouterView } from 'vue-router'

const route = useRoute()
const userName = ref(route.params.username)
const posts = ref([
  { id: 1 , title: 'Post 1' , content: 'Content 1' },
  { id: 2 , title: 'Post 2' , content: 'Content 2' },
  { id: 3 , title: 'Post 3' , content: 'Content 3' },
])

const router = useRouter()
const getPostDetail = function (postId) {
  console.log(postId)
  router.replace({ name: 'post-detail', params: { id: postId }})
}
</script>

<style scoped>

</style>