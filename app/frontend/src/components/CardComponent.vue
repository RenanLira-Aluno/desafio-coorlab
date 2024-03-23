<script setup lang="ts">
import { PhHandCoins, PhTruck } from '@phosphor-icons/vue';
import { ITripResponse } from '../services/GetBetterTrips';


const { type } = defineProps<{
    type: 'faster' | 'mostEconomic'
    trip: ITripResponse
}>()

</script>

<template>

    <div class="card">
        <div class="card-info">

            <div class="icon">
                <PhTruck :weight="'fill'" :size="40" v-if="type == 'faster'" />
                <PhHandCoins :weight="'fill'" :size="40" v-else-if="type == 'mostEconomic'" />
            </div>
            <div class="info">
                <h4>{{ trip.name }}</h4>

                <p v-if="type == 'faster'">Leito: {{ trip.bed }} </p>
                <p v-if="type == 'mostEconomic'">Poltrona: {{ trip.seat }} </p>

                <p>Tempo estimado: {{ trip.duration }}</p>
            </div>
        </div>

        <div class="card-price">
            <h4>Preço</h4>
            <p v-if="type == 'faster'">{{ trip.price_confort }}</p>
            <p v-else-if="type == 'mostEconomic'">{{ trip.price_econ }}</p>
        </div>
    </div>

</template>


<style scoped>
.card {
    @apply grid grid-cols-[2fr_1fr] gap-4 w-full;
}

.card-info {
    @apply flex w-full rounded-md overflow-hidden;
}

.info {
    @apply flex flex-col p-5 bg-slate-200 flex-[3];
}
.info h4 {
    @apply text-lg font-bold;
}
.icon {
    @apply flex justify-center items-center bg-blue-300 text-white flex-1;
}
.card-price {
    @apply flex flex-col p-5 bg-slate-200 flex-[1] rounded-md overflow-hidden justify-center;
}
.card-price h4 {
    @apply text-lg font-bold;
}
</style>