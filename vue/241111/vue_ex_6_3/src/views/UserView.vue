<template>
  <div>
    <h2>User Profile</h2>
    <p>Username: {{ username }}</p>

    <RouterLink :to="{ name: 'user-profile' }">상세 프로필</RouterLink> | 
    <RouterLink :to="{ name: 'user-posts' }">작성한 게시글</RouterLink>
    <hr>

    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, RouterLink, RouterView } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)
</script>
