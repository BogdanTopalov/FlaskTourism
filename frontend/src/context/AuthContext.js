import { createContext, useEffect, useState } from "react";
import { getUserDetails } from "../services/authRequests";


const useLocalStorage = (key, defaultValue) => {
    const [value, setValue] = useState(() => {
        const storedData = localStorage.getItem(key)

        return storedData ? JSON.parse(storedData) : defaultValue
    })

    const setLocalStorageValue = (newValue) => {
        localStorage.setItem(key, JSON.stringify(newValue))
        setValue(newValue)
    }

    return [value, setLocalStorageValue]
}


export const AuthContext = createContext()

export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useLocalStorage('auth', {})
    const [user, setUser] = useState({})

    const isAuthenticated = Boolean(auth.token)

    useEffect(() => {
        if (auth.token) {
            getUserDetails(auth.token)
                .then(result => {
                    setUser(result)
                })
        }
    }, [auth])

    const userLogin = (data) => {
        setAuth(data)
    }

    const userLogout = () => {
        setAuth({})
    }

    return (
        <AuthContext.Provider value={{ user, userLogin, userLogout, isAuthenticated}}>
            {children}
        </AuthContext.Provider>
    )
}