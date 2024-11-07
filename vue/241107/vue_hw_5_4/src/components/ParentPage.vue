<template>
  <div>
    <ChildPage
      v-for="(child, index) in children"
      :key="child.name"
      :child-props="child"
      @get-me-allowance="updateBalance(index)"
    />
  </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue'
import { ref } from 'vue'

const children = ref([
  {name: '김하나', age: 30, balance: 100000},
  {name: '김두리', age: 20, balance: 10000},
  {name: '김서이', age: 10, balance: 1000}
])

const updateBalance = function (index) {
  console.log('용돈 올리기')
  console.log(index)
  children.value[index].balance += 1000
}
</script>

<style scoped>

</style>