<template>
  <nav>
    <RouterLink :to="{ 'name': 'home' }"><a>HOME</a></RouterLink>
    <RouterLink :to="{ 'name': 'products' }">PRODUCTS</RouterLink>
    <RouterLink :to="{ 'name': 'favorite' }" id="alert-parent">
      FAVORITE 
      <div id="alert" v-show="store.favoriteCounts > 0">
        {{ store.favoriteCounts }}
      </div>
    </RouterLink>
  </nav>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useProductStore } from './stores/product';

const store = useProductStore()
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-evenly;
  background-color: rgb(41, 41, 41);
  padding: 15px;
}

nav > a {
  color: white;
  text-decoration: none;
}

#alert-parent {
  position: relative;
}

#alert {
  position: absolute;
  top: -5px;
  right: -30px;
  background-color: red;
  color: white; 
  border-radius: 50%; 
  width: 25px; 
  height: 25px; 
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
}
</style>
