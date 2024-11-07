<template>
  <div>
    <li>
      {{ cartList.name }} - {{ cartList.price }}원
      <button @click="deleteItem">삭제</button>
    </li>
  </div>
</template>

<script setup>
defineProps({ cartList: Object })

const emit = defineEmits(['deleteItem'])

const deleteItem = function() {
  emit('deleteItem')
}
</script>

<style scoped>

</style>