<script setup lang="ts">
import Calendar from 'primevue/calendar';
import { reactive } from "vue"
import { vMaska, MaskaDetail } from 'maska'

const { dateSelect, id, label } = defineProps<{
    dateSelect: ((event: Event) => void),
    id: string,
    label: string
}>()

const bindedValue = reactive({} as MaskaDetail)
const op = reactive({
    mask: '##/##/####',
    tokens: {
        '#': { pattern: /\d/ }
    }
})


</script>

<template>

    <div>
        <label :for="id">{{ label }}</label>
        <Calendar :input-id="id" v-maska:[op]="bindedValue" @input="dateSelect" v-model="bindedValue.masked"
            date-format="dd/mm/yy" :pt="{
            input: 'bg-white p-3 h-12 focus:outline-none w-full rounded-md overflow-hidden',
            panel: 'bg-white mt-3 p-4 flex flex-col gap-4 max-h-auto shadow-md rounded-md',
            header: 'flex justify-between items-center',
            title: 'text-lg font-bold flex gap-3',
            container: 'flex flex-col gap-4',
            group: 'flex flex-col gap-8',
            table: 'w-full flex flex-col',
            tableHeaderRow: 'flex flex-row justify-between items-center',
            tableBodyRow: 'flex flex-row justify-between items-center',
            tableHeaderCell: 'text-center flex-1',
            tableBodyCell: 'text-center flex-1',
            day: 'cursor-pointer hover:bg-gray-100 p-2 rounded-md transition-colors duration-200 ease-in-out text-center flex-1',
            month: 'cursor-pointer hover:bg-gray-100 p-2 rounded-md transition-colors duration-200 ease-in-out text-center flex-1',
            year: 'cursor-pointer hover:bg-gray-100 p-2 rounded-md transition-colors duration-200 ease-in-out text-center flex-1',
        }" />
    </div>

</template>