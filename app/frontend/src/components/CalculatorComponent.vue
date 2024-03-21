<script setup lang="ts">
import { PhTruck, PhHandCoins } from '@phosphor-icons/vue'
import { AvaliableCitiesService } from '../services/AvaliableCitiesService'
import { onMounted, ref } from 'vue';
import AutoCompleteComponent from './AutoCompleteComponent.vue';

const props = defineProps<{
    title: string
    subtitle: string
}>()



const cities = ref<{ id: number, name: string }[]>([])


onMounted(async () => {
    cities.value = await AvaliableCitiesService.getData()
})



</script>

<template>
    <div class="container">
        <div class="header">
            <PhTruck :weight="'fill'" :size="40" />
            <h2>
                {{ props.title }}
            </h2>
        </div>
        <div class="body">
            <form>
                <div class="form-title">
                    <PhHandCoins :weight="'fill'" />
                    <h3>{{ props.subtitle }}</h3>
                </div>

                <div class="form-section">
                    <AutoCompleteComponent :options="cities" />
                </div>

                <div class="form-section">
                    <label for="date">Date</label>
                    <input type="date" id="date" />
                </div>

                <div class="form-section">
                    <button type="submit">Calcular</button>
                </div>
            </form>
            <div class="result">
                <p>Nenhum Dado Selecionado</p>
            </div>
        </div>
    </div>

</template>

<style scoped>
autoCompleteStyle {
    width: '100%'
}

.header {
    @apply flex w-full h-20 bg-slate-500 text-white items-center gap-4 px-10 text-2xl font-bold;
}

.container {
    @apply flex flex-col w-full h-full shadow-xl rounded-md overflow-hidden;
}

.body {
    @apply flex gap-4 px-4 py-10 h-full;
}

form {
    @apply flex flex-col gap-4 p-20 bg-slate-300 flex-1 justify-center;
}

.form-section {
    @apply flex flex-col gap-2;
}

.form-title {
    @apply flex items-center gap-2;
}

.result {
    @apply flex flex-1
}
</style>