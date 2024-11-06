<template>
  <card style="text-align: center; border: solid 1px black; padding: 30px; margin: 15px; width: 300px;">

    <h1>가수 이름</h1>
    <div>
      <img src="@/assets/singer.jpg" alt="" style="width: 200px; border-radius: 70%;">
    </div>
    <p>가수 소개글</p>
    <div style="display: flex; justify-content: center;">
      <SingerAlbum />
      <SingerAlbum />
    </div>

  </card>

</template>

<script setup>
import SingerAlbum from '@/components/singers/SingerAlbum.vue';
</script>

<style scoped>
h1 {
  color: green;
}
</style>