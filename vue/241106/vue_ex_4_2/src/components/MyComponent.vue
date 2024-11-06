<template>
  <div>
    <header class="sticky-top container text-center">
      <h1 class="align-items-center">Gallery</h1>
    </header>

    <main>
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
        <div class="col" v-for="number in numberOfItems">
          <div class="card">
            <img src="@/assets/sample.png" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const numberOfItems = ref(4)
</script>

<style scoped>

</style>
