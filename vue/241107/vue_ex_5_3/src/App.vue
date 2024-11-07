<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList
      :products="products" 
      @add-to-cart="addToCart"
    />
    <h3>총 가격: {{ totalPrice }}원</h3>

    <h1>장바구니</h1>
    <ul>
      <Cart
        v-for="(cartList, index) in cartLists"
        :key="cartList.id"
        :cart-list="cartList"
        @delete-item="deleteItem(index)"
      />
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue';

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const totalPrice = ref(0)
const cartLists = ref([])

const addToCart = function (index) {
  console.log(index)
  cartLists.value.push({
    name: products.value[index].name,
    price: products.value[index].price
  })
  totalPrice.value += products.value[index].price
}

const deleteItem = function (index) {
  totalPrice.value -= cartLists.value[index].price
  cartLists.value.splice(index, 1)
  
}

</script>
