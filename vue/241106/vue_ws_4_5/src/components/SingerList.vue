<template>
  <div style="text-align: center;">
    <img src="@/assets/microphone.jpg" alt="" width="200">
    <h1>가수 목록</h1>
  </div>
  <div v-for="singer in singers" style="display: flex; flex-wrap: wrap; justify-content: center;">
    <div style="box-sizing: border-box; padding: 10px;">
      <SingerDetail />
    </div>
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue';
import { ref } from 'vue'

const singers = ref([
  {name: 'adele'},
  {name: 'maroon5'},
  {name: 'Dua Lipa'},
])
</script>

<style scoped>
  card {
    display: inline-block;
    width: 40%;
    margin: 20px;
  }

  h1 {
    color: orange;
  }
</style>
