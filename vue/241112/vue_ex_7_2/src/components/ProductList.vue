<template>
  <div>
    <h2>Product List</h2>
    <ul>
      <li v-for="product in store.products" :key="product.id">
        <ProductListItem :product="product" />
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'
import ProductListItem from '@/components/ProductListItem.vue';

const store = useProductStore()
</script>
