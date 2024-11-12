<template>
  <div id="maindiv">
    <h2>메인 페이지</h2>
    <MainPage
      v-for="balanceInfo in store.balances"
      :key="balanceInfo.name"
      :balance-info="balanceInfo"
    />
  </div>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';
import { useBalanceStore } from '@/stores/balance';

const store = useBalanceStore()

</script>

<style scoped>
#maindiv {
  padding: 20px;
}
</style>