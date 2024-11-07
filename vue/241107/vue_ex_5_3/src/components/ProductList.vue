<template>
  <ul>
    <ProductListItem 
      v-for="(product, index) in products" 
      :key="product.id" 
      :product="product"
      @add-to-cart="addToCart(index)"
    />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'

defineProps({
  products: Array
})

const emit = defineEmits(["addToCart"])
const addToCart = function (index) {
  emit("addToCart", index)
}
</script>
