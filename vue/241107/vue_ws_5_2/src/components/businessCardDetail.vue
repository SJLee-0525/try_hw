<template>
  <div>
    <h3>이름: {{ businessCard.name }}</h3>
    <h1>직함: {{ businessCard.title }}</h1>
  </div>
</template>

<script setup>

import BusinessCard from './BusinessCard.vue';
defineProps({
  businessCard: Object
})
</script>

<style scoped>
div {
  background-color: rgb(202, 202, 201);
  border: 1px gray solid;
  margin: 20px;
  width: 500px;
  text-align: center;
}
</style>