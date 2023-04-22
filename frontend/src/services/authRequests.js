import { post } from "./requests"

const apiUrl = 'http://127.0.0.1:5000'

export const login = (email, password) => {
    return post(`${apiUrl}/login`, { email, password })
}

export const logout = async (token) => {
    try {
        const response = await fetch(`${apiUrl}/logout`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
        return response
    } catch (error) {
        
    }
}

export const register = (first_name, last_name, email, password) => {
    return post(`${apiUrl}/register`, {first_name, last_name, email, password})
}

export const getUserDetails = (token) => {
    return post(`${apiUrl}/user`, {token})
}