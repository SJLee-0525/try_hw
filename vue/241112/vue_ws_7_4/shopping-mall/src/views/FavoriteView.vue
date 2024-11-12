<template>
  <div>
    <h1>장바구니 페이지</h1>
    <main>
      <div v-for="product in store.favoriteProductList" :key="product.name">
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
      </div>
    </main>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
const store = useProductStore()

</script>

<style scoped>
main {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

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
