<script setup lang="ts">
import MenuComponent from './components/MenuComponent.vue'
</script>

<template>
    <div class="app">
        <MenuComponent />
        <RouterView />
    </div>
</template>

<style scoped>
.app {
    @apply flex h-screen w-screen;
}
</style>
