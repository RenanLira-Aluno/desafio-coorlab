<script setup lang="ts">
import { PhWarningCircle } from '@phosphor-icons/vue';
import Dialog from 'primevue/dialog';

const { visible, close } = defineProps<{ visible: boolean, close: () => void }>()

</script>

<template>
    <Dialog :visible="visible" modal :closable="false" :style="{ width: '32vw' }" :pt="{
        root: 'p-4 bg-white flex justify-between items-center flex-col rounded-md h-96',
        footer: 'p-4 w-full',
        mask: 'bg-black bg-opacity-50'
    }">
        <div class="content">
            <PhWarningCircle :size="80" :weight="'fill'" />
            <p>Insira os valores para carregar a cotação.</p>
        </div>
        <template #footer>
            <button type="button" @click="close">Fechar</button>
        </template>
    </Dialog>
</template>

<style scoped>
button {
    @apply p-2 bg-slate-400 text-white rounded-md w-full font-bold text-lg;
}

.content {
    @apply flex flex-col items-center gap-4;
}

p {
    @apply text-2xl font-bold;
}
</style>