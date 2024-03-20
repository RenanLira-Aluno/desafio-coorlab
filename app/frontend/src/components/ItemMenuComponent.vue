<script setup lang="ts">
import { PhMathOperations } from '@phosphor-icons/vue'
import { RouterLink } from 'vue-router'

const props = defineProps({
    title: { type: String, required: true }
})
</script>

<template>
    <RouterLink to="/calculadora">
        <li>
            <PhMathOperations class="h-6 w-6" :weight="'fill'" />
            <span>{{ props.title }}</span>
        </li>
    </RouterLink>
</template>

<style scoped>
li {
    @apply flex items-center gap-2;
}

span {
    @apply font-bold text-lg
}
</style>