<template>
  <div style="text-align: center;">
    <img src="@/assets/microphone.jpg" alt="" width="200">
    <h1>가수 목록</h1>
  </div>
  <SingerDetail />
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue';
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
