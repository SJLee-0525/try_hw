<template>
  <div>
    <h1>상품 목록 페이지</h1>
    <main>
      <ProductDetail
        v-for="product in store.productList"
        :key="product.name"
        :product="product"
      />
    </main>
  </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue';
import { useProductStore } from '@/stores/product';

const store = useProductStore()

</script>

<style scoped>
main {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>