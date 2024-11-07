<template>
  <div style="display: flex; justify-content: center; flex-direction: column;">
    <h2 style="text-align: center;">보유 명함 목록</h2>
    <div style="display: flex; flex-wrap: wrap; justify-content: center;">
    <businessCardDetail
      v-for="businessCard in businessCards"
      :key="businessCard.name"
      :business-card="businessCard"
      @delete-card-event="deleteCard"
    />
  </div>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import businessCardDetail from '@/components/businessCardDetail.vue';

const businessCards = ref([
  {name: '일론 머스크', title: '테슬라 테크노킹'},
  {name: '래리 앨리슨', title: '오라클 창업주'},
  {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
  {name: '래리 페이지', title: '구글 공동창업주'},
  {name: '세르게이 브린', title: '구글 공동창업주'}
])

const deleteCard = function (BusinessCard) {
  const targetIndex = businessCards.value.some((card, index) => {
    console.log(card.name)
    if (card.name === BusinessCard.name) {
      return index
    }
  })
  businessCards.value.splice(targetIndex, 1)
}
</script>

<style scoped>

</style>