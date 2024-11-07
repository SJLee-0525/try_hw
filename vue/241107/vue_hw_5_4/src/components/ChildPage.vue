<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름: {{ childProps.name }}</p>
    <p>나이: {{ childProps.age }}</p>
    <p>용돈: {{ childProps.balance }}</p>
    <button @click="giveMeAllowance">용돈 주세요</button>
  </div>
</template>

<script setup>
defineProps({
  childProps: Object
})
const emit = defineEmits(['getMeAllowance'])

const giveMeAllowance = function() {
  emit('getMeAllowance')
}
</script>

<style scoped>

</style>