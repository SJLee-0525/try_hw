<template>
  <div>
    <h1>Product List</h1>
    <ul v-for="product in store.products">
      <li>
        <p>{{ product.id }} - {{ product.title }} - {{ product.body }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';

const store = useProductStore()
</script>

<style scoped>

</style>