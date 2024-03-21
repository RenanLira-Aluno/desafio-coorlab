import axios from "axios"

type IAvaliableCitiesResponse = string[]

export const AvaliableCitiesService = {

    async getData() {
        const res = await axios.get<IAvaliableCitiesResponse>('http://127.0.0.1:3000/trips/avaliable-cities')

        const data = res.data.map((v, i) => {
            return {
                id: i,
                name: v
            }
        })

        return data
    }

}