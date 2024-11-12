<template>
  <div>
    <h1>데이터 수정 페이지</h1>

    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="increaseBalance">+</button>

  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useBalanceStore } from '@/stores/balance';
const balanceStore = useBalanceStore()

const route = useRoute()
const targetName = route.params.name

const balance = balanceStore.findBalance(targetName)

const increaseBalance = () => {
  balanceStore.increaseBalance(targetName)
}
</script>

<style scoped>

</style>