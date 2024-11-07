<template>
  <div> 
    <h3>자식 페이지입니다</h3>
    <p>이름: {{ childProps.name }}</p>
    <p>나이: {{ childProps.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  childProps: Object
})
</script>

<style scoped>

</style>