import axios from "axios"

export interface ITripResponse {
    bed: string
    city: string
    duration: string
    id: number
    name: string
    price_confort: string
    price_econ: string
    seat: string
}

export interface IGetBetterTripsResponse {
    faster: ITripResponse
    mostEconomic: ITripResponse
}

export const GetBetterTripsService = {

    async get(city: string, date: string) {
        const res = await axios.get<IGetBetterTripsResponse>(`http://127.0.0.1:3000/trips/comfortable-or-economic?city=${city}&date=${date}`)

        return res.data
    }
}