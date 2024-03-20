<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
    <RouterLink to="/" class="logo">
        <img src="/logo.png" alt="">
    </RouterLink>
</template>

<style scoped>
.logo {
    @apply flex h-auto w-60;
}
</style>