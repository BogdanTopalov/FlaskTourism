import { get, post, put } from "./requests"


const apiUrl = 'http://127.0.0.1:5000'

export const createReservation = (hotel_id, nights) => {
    return post(`${apiUrl}/reservations/create`, {hotel_id, nights})
}

export const getAllReservations = () => {
    return get(`${apiUrl}/reservations`)
}

export const updateReservation = (id) => {
    return put(`${apiUrl}/reservations/update/${id}`)
}