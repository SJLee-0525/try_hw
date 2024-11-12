<template>
  <div>
    <p>이름 : {{ balanceInfo.name }}</p>
    <p>잔고 : {{ balanceInfo.balance }}</p>
    <button @click="goUpdateView(balanceInfo.name)">updateBalance</button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
defineProps({
  balanceInfo: Object
})

const router = useRouter()
const goUpdateView = function (balanceName) {
  console.log(balanceName)
  router.push({ name: 'update', params: { 'name': balanceName } })
}
</script>

<style scoped>

</style>