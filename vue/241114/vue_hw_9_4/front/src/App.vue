<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from './stores/articles';

const store = useArticleStore()
console.log(store.isLogin)
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink :to="{ name: 'home' }">Home</RouterLink>
        <span v-show="!store.isLogin">
          | 
          <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink> |
          <RouterLink :to="{ name: 'signin' }">SignIn</RouterLink> |
        </span>
      </nav>
      <div>
      <h3 v-if="store.isLogin">안녕하세요</h3>
      <h3 v-else>로그아웃 됨</h3>
    </div>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
