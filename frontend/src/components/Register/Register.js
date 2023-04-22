import { useState, useContext } from "react"
import { register } from "../../services/authRequests"
import { AuthContext } from "../../context/AuthContext"
import { useNavigate } from "react-router-dom"
import styles from "./Register.module.css"


const Register = () => {

    const initialValues = { firstName: '', lastName: '', email: '', password: '' }
    const [formValues, setFormValues] = useState(initialValues)
    const { userLogin } = useContext(AuthContext)
    const navigate = useNavigate()

    const onChangeHandler = (e) => {
        const { name, value } = e.target
        setFormValues(
            { ...formValues, [name]: value }
        )
    }

    const onSubmit = (e) => {
        e.preventDefault()

        register(formValues.firstName, formValues.lastName, formValues.email, formValues.password)
            .then(result => {
                userLogin(result)
                navigate('/')
            })
    }

    return (
        <div className={styles.register}>
            <form onSubmit={onSubmit}>
                <input type="text" name="firstName" placeholder="firstName" onChange={onChangeHandler} />
                <input type="text" name="lastName" placeholder="lastName" onChange={onChangeHandler} />
                <input type="email" name="email" placeholder="email" onChange={onChangeHandler} />
                <input type="password" name="password" placeholder="password" onChange={onChangeHandler} />
                <button>Register</button>
            </form>
        </div>
    )
}

export default Register