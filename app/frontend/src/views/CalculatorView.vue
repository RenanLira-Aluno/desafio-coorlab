<script setup lang="ts">
import Calculator from '../components/CalculatorComponent.vue'
</script>


<template>
    <div class="page">
        <Calculator title="Calculadora de Viagem" subtitle="Calcule o Valor da Viagem" />
    </div>
</template>

<style scoped>
.page {
    @apply flex w-full items-center justify-center px-32 py-40;
}
</style>