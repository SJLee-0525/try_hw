<template>
  <div id="card">
    <p><strong>{{ product.name }}</strong></p>
    <div id="imgdiv">
      <img :src="product.imagePath" alt="상품 이미지">
    </div>
    <p>￦ {{ product.price }}</p>
    <div>
      <span @click="callToggleFavorite(product.name)" v-show="!product.isFavorite">🤍</span>
      <span @click="callToggleFavorite(product.name)" v-show="product.isFavorite">❤️</span>
    </div>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
const store = useProductStore()

defineProps({
  product: Object
})

const callToggleFavorite = function (productName) {
  console.log(store.productList)
  store.toggleFavorite(productName)
}
</script>

<style scoped>
img {
  width: 300px;
  align-self: center;
}

#imgdiv {
  display: flex;
  height: 230px;
}

#card {
  text-align: center;
  border: solid rgb(185, 185, 185) 1px;
  margin: 10px;
  padding: 10px;
}
</style>