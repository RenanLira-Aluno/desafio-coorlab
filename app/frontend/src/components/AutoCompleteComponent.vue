<script setup lang="ts">
import AutoComplete, { AutoCompleteCompleteEvent, AutoCompleteItemSelectEvent } from 'primevue/autocomplete';
import { ref } from 'vue';

const { options, change, id, label } = defineProps<{
    options: string[],
    id: string,
    label: string,
    change: ((event: AutoCompleteItemSelectEvent) => void)
}>()


const filteredOptions = ref<string[]>([])
const selectInput = ref<string>('')

const search = (event: AutoCompleteCompleteEvent) => {
    setTimeout(() => {
        if (!event.query.trim().length) {
            filteredOptions.value = [...options];
        } else {
            filteredOptions.value = options.filter((op) => {
                return op.toLowerCase().includes(event.query.toLowerCase());
            });
        }
    }, 250);
}

</script>

<template>
    <div>
        <label :for="id">{{ label }}</label>
        <AutoComplete :input-id="id" v-model="selectInput" force-selection v-on:item-select="change"
            :suggestions="filteredOptions" @complete="search" :pt="{
            input: 'bg-white p-3 h-12 focus:outline-none w-full rounded-md overflow-hidden',
            list: 'bg-white mt-3 p-4 flex flex-col gap-4 overflow-y-scroll max-h-60 w-full shadow-md rounded-md',
            root: 'flex relative items-center',
            loadingIcon: 'absolute right-3 ',
            item: 'cursor-pointer hover:bg-gray-100 p-2 rounded-md transition-colors duration-200 ease-in-out',

        }" />
    </div>
</template>

<style scoped></style>
