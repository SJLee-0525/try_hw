<template>
  <div>
    <h1>자식 페이지</h1>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: Object
})
</script>

<style scoped>
div {
  border: solid rgb(173, 173, 173) 1px;
  background-color: rgb(255, 255, 255);
  text-align: center;
  padding: 10px;
  margin: 10px;
}
</style>