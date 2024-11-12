import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  const productList = ref([
    {
      name: '상품 1',
      imagePath: 'src/assets/product1.png',
      price: 10000,
      isFavorite: true
    },
    {
      name: '상품 2',
      imagePath: 'src/assets/product2.png',
      price: 20000,
      isFavorite: false
    },
    {
      name: '상품 3',
      imagePath: 'src/assets/product3.png',
      price: 30000,
      isFavorite: false
    },
    {
      name: '상품 4',
      imagePath: 'src/assets/product4.png',
      price: 40000,
      isFavorite: false
    },
  ])

  const favoriteCounts = computed(() => {
    const checkProductList = productList.value.filter((product) => product.isFavorite === true)
    return checkProductList.length
  })

  const favoriteProductList = computed(() => {
    const checkedProductList = productList.value.filter((product) => product.isFavorite === true)
    return checkedProductList
  })
  
  const toggleFavorite = function (targetProductName) {
    productList.value = productList.value.map((product) => {
      if (product.name === targetProductName) {
        product.isFavorite = !product.isFavorite
      }
      return product
    })
  }

  return { productList, favoriteCounts, favoriteProductList, toggleFavorite }
})
