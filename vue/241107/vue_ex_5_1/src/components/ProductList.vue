<template>
  <div>
    <li v-for="productProp in productProps">
      {{ productProp.name }} - {{ productProp.price }}
    </li>
  </div>
</template>

<script setup>
defineProps({productProps:Array})
</script>

<style scoped>

</style>