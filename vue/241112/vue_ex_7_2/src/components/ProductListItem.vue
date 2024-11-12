<template>
  <div>
    <a>{{ product.id }} - {{ product.title }} - {{ product.body }}</a>
    <button @click="callDeleteProduct(product.id)">DELETE</button>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';

defineProps({
  product: Object,
})

const store = useProductStore()

const callDeleteProduct = function (productId) {
  store.deleteProduct(productId)
}
</script>

<style scoped>

</style>