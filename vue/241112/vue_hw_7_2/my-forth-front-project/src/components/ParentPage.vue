<template>
  <div>
    <h1>부모 컴포넌트</h1>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage
      v-for="child in family.children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue';

defineProps({
  family: Object
})
</script>

<style scoped>
div {
  border: solid rgb(173, 173, 173) 1px;
  background-color: rgb(236, 235, 235);
  text-align: center;
  padding: 10px;
  margin: 10px;
}
</style>