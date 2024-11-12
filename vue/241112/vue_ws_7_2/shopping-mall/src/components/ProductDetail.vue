<template>
  <div id="card">
    <p><strong>{{ product.name }}</strong></p>
    <div id="imgdiv">
      <img :src="product.imagePath" alt="상품 이미지">
    </div>
    <p>￦ {{ product.price }}</p>
    <p v-show="!product.isFavorite">🤍</p>
    <p v-show="product.isFavorite">❤️</p>
  </div>
</template>

<script setup>
defineProps({
  product: Object
})
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