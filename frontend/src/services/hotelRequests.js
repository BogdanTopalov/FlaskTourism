import { del, get, post, put } from "./requests"


const apiUrl = 'http://127.0.0.1:5000'

export const getAllHotels = () => {
    return get(`${apiUrl}/hotels`)
}

export const getSingleHotel = (id) => {
    return get(`${apiUrl}/hotels/${id}`)
}

export const addHotel = (name, stars, country, city, image_url, price_per_night) => {
    return post(`${apiUrl}/hotels/add`, {name, stars, country, city, image_url, price_per_night})
}

export const updateHotel = (id, name, stars, country, city, image_url, price_per_night) => {
    return put(`${apiUrl}/hotels/update/${id}`, {name, stars, country, city, image_url, price_per_night})
}

export const deleteHotel = (id) => {
    return del(`${apiUrl}/hotels/delete/${id}`)
}
