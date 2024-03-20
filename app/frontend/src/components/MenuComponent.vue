<script setup lang="ts">
import Logo from './Logo.vue'
</script>

<template>
    <div class="menu">
        <Logo />
        <nav>
            <ul>
                <li class="item-menu">Calculadora de Viagem</li>
            </ul>
        </nav>
    </div>
</template>

<style scoped>
.item-menu {
    @apply p-4;
}

.menu {
    @apply p-8 h-screen flex bg-fuchsia-300 w-1/5 flex-col items-start;
}
</style>