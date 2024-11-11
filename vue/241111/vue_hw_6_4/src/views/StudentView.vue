<template>
  <div>
    <h1>학생 상세 정보 목록입니다.</h1>
    <ul v-for="student in students" :key="student.name">
      <li>
        <a @click="goStudentPush(student.name)">{{ student.name }} 학생 정보 보기</a>
      </li>
    </ul>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'

const students = ref([
  { name: '김하나' },
  { name: '김두리' },
  { name: '김서이' },
])

const router = useRouter()
const goStudentPush = function (studentName) {
  router.push({ name: 'studentDetail', params: { name: studentName } })
}
</script>

<style scoped>

</style>