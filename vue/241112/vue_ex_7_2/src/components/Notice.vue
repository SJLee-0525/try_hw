<template>
  <div>
    <h3>남은 제품 개수 : {{ store.productCount }}</h3>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';

const store = useProductStore()

</script>

<style scoped>

</style>