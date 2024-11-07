<template>
  <div>
    <h3 style="margin: 0;">이름: {{ businessCard.name }}</h3>
    <p>직함: {{ businessCard.title }}</p>
    <button @click="deleteCardFunc(businessCard)">명함 삭제</button>
  </div>
</template>

<script setup>

import BusinessCard from './BusinessCard.vue';
defineProps({
  businessCard: Object
})

const emit = defineEmits(["deleteCardEvent"])
const deleteCardFunc = function (businessCard) {
  console.log(businessCard)
  emit("deleteCardEvent", businessCard)
}
</script>

<style scoped>
div {
  background-color: ghostwhite;
  border: 1px rgb(196, 195, 195) solid;
  margin: 20px;
  padding: 30px;
  width: 500px;
  text-align: center;
}
</style>