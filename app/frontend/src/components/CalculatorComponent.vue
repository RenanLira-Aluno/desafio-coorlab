<script setup lang="ts">
import { PhTruck, PhHandCoins } from '@phosphor-icons/vue'
import { AvaliableCitiesService } from '../services/AvaliableCitiesService'
import { onMounted, ref } from 'vue';
import AutoCompleteComponent from './AutoCompleteComponent.vue';
import DateSelectComponent from './DateSelectComponent.vue';
import { AutoCompleteItemSelectEvent } from 'primevue/autocomplete';

const props = defineProps<{
    title: string
    subtitle: string
}>()



const cities = ref<string[]>([])
const selectedCity = ref<string>('')
const selectedDate = ref<string>('')

onMounted(async () => {
    const res = await AvaliableCitiesService.getData()

    cities.value.push(...res)
})


// event functions
const change = (event: AutoCompleteItemSelectEvent) => {
    selectedCity.value = event.value
}

const dateSelect = (event: Event) => {
    selectedDate.value = (event.target as HTMLInputElement)?.value
}

const onSubmit = (event: Event) => {
    event.preventDefault()
    console.log(selectedCity.value, selectedDate.value)
}

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
            <form :on-submit="onSubmit" action="/calculadora">
                <div class="form-title">
                    <PhHandCoins :weight="'fill'" />
                    <h3>{{ props.subtitle }}</h3>
                </div>

                <div class="form-section">
                    <AutoCompleteComponent :options="cities" :change="change" label="Selecione uma cidade" id="city" />
                </div>

                <div class="form-section">
                    <DateSelectComponent :date-select="dateSelect" id="date" label="Selecione uma data" />
                </div>

                <div class="form-section">
                    <button type="submit" @click="onSubmit">calcular</button>
                </div>
            </form>
            <div class="result">
                <p>Nenhum Dado Selecionado</p>
            </div>
        </div>
    </div>

</template>

<style scoped>
.container {
    @apply flex flex-col w-full h-full shadow-xl rounded-md overflow-hidden;
}

.header {
    @apply flex w-full min-h-20 bg-slate-500 text-white items-center gap-4 px-10 text-2xl font-bold;
}


.body {
    @apply grid grid-cols-2 gap-2 px-4 py-10 flex-1;
}

form {
    @apply flex flex-col gap-8 p-20 bg-slate-300 justify-center rounded-md;
}

.form-section {
    @apply flex flex-col gap-2;
}

.form-title {
    @apply flex items-center gap-4 text-2xl justify-center font-bold;
}

.result {
    @apply flex shadow-xl;
}

button {
    @apply bg-slate-500 text-white p-4 rounded-md;
}
</style>