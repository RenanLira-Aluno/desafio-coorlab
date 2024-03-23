import axios from "axios"

type IAvaliableCitiesResponse = string[]

export const AvaliableCitiesService = {

    async get() {
        const res = await axios.get<IAvaliableCitiesResponse>('http://127.0.0.1:3000/trips/avaliable-cities')

        return res.data
    }

}