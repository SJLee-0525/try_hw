<template>
  <div style="display: flex; justify-content: center;">
    <form @submit.prevent="createCardFunc">
      <input type="text" label="이름" v-model="nameInput">
      <input type="text" label="직함" v-model="workInput">
      <input type="submit" value="명함 추가">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const nameInput = ref('')
const workInput = ref('')

const emit = defineEmits(['createCardEvent'])

const createCardFunc = function () {
  const cardInfo = ref({
    name: nameInput.value,
    title: workInput.value
  })
  emit('createCardEvent', cardInfo.value)
  
  nameInput.value = ''
  workInput.value = ''
}

</script>

<style scoped>
input {
  margin: 5px;
}
</style>