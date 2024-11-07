<template>
  <div>
    <form action="">
      {{ product.name }} - {{ product.price }}원
      <input type="button" value="장바구니에 추가"></input>
    </form>
  </div>
</template>

<script setup>
defineProps({
  product: Object
})
</script>

<style scoped>

</style>