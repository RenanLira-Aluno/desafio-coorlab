<script setup lang="ts">
import { PhTruck, PhHandCoins } from '@phosphor-icons/vue'
import { AvaliableCitiesService } from '../services/AvaliableCitiesService'
import { GetBetterTripsService, IGetBetterTripsResponse } from '../services/GetBetterTrips'
import { onMounted, ref } from 'vue';
import AutoCompleteComponent from './AutoCompleteComponent.vue';
import DateSelectComponent from './DateSelectComponent.vue';
import { AutoCompleteItemSelectEvent } from 'primevue/autocomplete';
import CardComponent from './CardComponent.vue';
import ErrorDialog from './ErrorDialog.vue';

const props = defineProps<{
    title: string
    subtitle: string
}>()



const cities = ref<string[]>([])
const selectedCity = ref<string>('')
const selectedDate = ref<string>('')
const inError = ref<boolean>(false)

const resultData = ref<IGetBetterTripsResponse | undefined>(undefined)

onMounted(async () => {
    const res = await AvaliableCitiesService.get()

    cities.value.push(...res)
})


// event functions
const citySelect = (event: AutoCompleteItemSelectEvent) => {
    selectedCity.value = event.value
}

const dateSelect = (event: Event) => {
    selectedDate.value = (event.target as HTMLInputElement)?.value
}

const onCloseError = () => {
    console.log('close')
    inError.value = false
}

const onSubmit = async (event: Event) => {
    event.preventDefault()

    if (!selectedCity.value || !selectedDate.value) {
        inError.value = true
        return
    }

    const res = await GetBetterTripsService.get(selectedCity.value, selectedDate.value)

    resultData.value = res
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
                    <PhHandCoins :weight="'fill'" :size="50" />
                    <h3>{{ props.subtitle }}</h3>
                </div>

                <div class="form-section">
                    <AutoCompleteComponent :options="cities" :change="citySelect" label="Selecione uma cidade"
                        id="city" />
                </div>

                <div class="form-section">
                    <DateSelectComponent :date-select="dateSelect" id="date" label="Selecione uma data" />
                </div>

                <div class="form-section">
                    <button type="submit" @click="onSubmit">CALCULAR</button>
                </div>
            </form>
            <div v-if="resultData" class="result">

                <CardComponent type="faster" :trip="resultData.faster" />
                <CardComponent type="mostEconomic" :trip="resultData.mostEconomic" />

            </div>
            <div v-else class="wait-result">
                <p>Nenhum dado selecionado.</p>
            </div>
        </div>
        <ErrorDialog :visible="inError" :close="onCloseError" />
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
    @apply flex flex-col gap-8 px-20 bg-slate-300 justify-center rounded-md;
}

.form-section {
    @apply flex flex-col gap-2;
}

.form-title {
    @apply flex items-center gap-4 text-3xl justify-center font-bold;
}

.result {
    @apply flex flex-col justify-center items-center p-8 rounded-md w-full gap-8;
}

.wait-result {
    @apply flex justify-center items-center p-8 rounded-md w-full gap-8;
}

.wait-result p {
    @apply text-2xl font-bold;
}

button {
    @apply bg-slate-500 text-white p-4 rounded-md;
}
</style>