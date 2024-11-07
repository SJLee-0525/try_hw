<template>
  <header style="position: relative; top: 30; display: flex; justify-content: center; text-align: center;">
    <div id="main" style="width: 50%;">
      <h1>명함 관리 페이지</h1>
    </div>
  </header>
  <main>
    <p style="text-align: center;">명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
  </main>
  <article style="display: flex; justify-content: center; flex-direction: column;">
    <CreateCardForm
      @create-card-event="updateCard"
    />
    <BusinessCard
      :new-card="newCard"
    />
  </article>
  <footer style="position: absolute; bottom: 0; width: 100%; text-align: center; background-color: ghostwhite;">
    <p>ⓒ2024 My Business Cards</p>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import CreateCardForm from '@/components/CreateCardForm.vue';
import BusinessCard from '@/components/BusinessCard.vue';

const newCard = ref()
const updateCard = function (cardInfo) {
  newCard.value = cardInfo
}
</script>

<style scoped>
#main {
  background-color: darkblue;
  color: white;
}
</style>
