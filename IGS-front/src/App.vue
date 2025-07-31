<template>
  <div class="app-container">
    <AppSidebar />
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="js">
import AppSidebar from './components/AppSidebar.vue';
</script>

<style scoped>
.app-container {
  display: flex;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  background-color: #F7F8FA;
  margin-left: 250px;
  min-height: 100vh;
}
</style>
