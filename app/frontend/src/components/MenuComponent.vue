<script setup lang="ts">
import Logo from './LogoComponent.vue'
import ItemMenu from './ItemMenuComponent.vue'
</script>

<template>
    <div class="menu">
        <Logo />
        <nav>
            <ul>
                <ItemMenu title="Calculadora de Viagem" />
            </ul>
        </nav>
    </div>
</template>

<style scoped>
.menu {
    @apply p-8 h-screen flex bg-slate-600 min-w-[360px] flex-col items-start gap-6 text-white;
}
</style>