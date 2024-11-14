<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="submitData">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title">

      <label for="content">내용 : </label>
      <input type="text" id="content" v-model="content">

      <button @submit.prevent="submitData">create</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/articles.js'
import { useRouter } from 'vue-router'

const store = useArticleStore()
const router = useRouter()

const title = ref('')
const content = ref('')

const submitData = function () {
  const article = {
    title: title.value,
    content: content.value
  }
  store.createArticle(article)
  title.value = ''
  content.value = ''
  router.push({ name: 'home' })
}

</script>

<style lang="scss" scoped>

</style>