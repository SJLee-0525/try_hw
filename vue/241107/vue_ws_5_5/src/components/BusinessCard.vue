<template>
  <div style="display: flex; justify-content: center; flex-direction: column;">
    <h2 style="text-align: center;">보유 명함 목록</h2>
    <p style="text-align: center;">현재 보유 중인 명함 수: {{ businessCardsCount }}</p>
    <div v-if="businessCardsCount > 0" style="display: flex; flex-wrap: wrap; justify-content: center;">
    <businessCardDetail
      v-for="businessCard in businessCards"
      :key="businessCard.name"
      :business-card="businessCard"
      @delete-card-event="deleteCard"
    />
  </div>
  <div v-else>
    <p style="text-align: center;">명함이 없습니다. 새로운 명함을 추가해 주세요</p>
  </div>
  </div>

</template>

<script setup>
import { ref, computed, watch } from 'vue'
import businessCardDetail from '@/components/businessCardDetail.vue';

const props = defineProps({
  newCard: Object
})
const businessCards = ref([
  {name: '일론 머스크', title: '테슬라 테크노킹'},
  {name: '래리 앨리슨', title: '오라클 창업주'},
  {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
  {name: '래리 페이지', title: '구글 공동창업주'},
  {name: '세르게이 브린', title: '구글 공동창업주'}
])

const businessCardsCount = computed(() => {
  return businessCards.value.length
})

const deleteCard = function (BusinessCard) {
  const targetIndex = businessCards.value.some((card, index) => {
    console.log(card.name)
    if (card.name === BusinessCard.name) {
      return index
    }
  })
  businessCards.value.splice(targetIndex, 1)
}

watch(() => props.newCard, (card) => businessCards.value.push(card))
</script>

<style scoped>

</style>