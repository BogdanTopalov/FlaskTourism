import { useContext, useState } from "react"
import { login } from "../../services/authRequests"
import { useNavigate } from "react-router-dom"
import { AuthContext } from "../../context/AuthContext"
import styles from "./Login.module.css"


const Login = () => {

    const initialValues = {firstName:'', lastName:'', email: '', password: ''}
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

        login(formValues.email, formValues.password)
            .then(data => {
                userLogin(data)
                navigate('/')
            })
    }

    return (
        <div className={styles.login}>
        <form onSubmit={onSubmit}>  
            <input type="email" name="email" placeholder="email" onChange={onChangeHandler}/>
            <input type="password" name="password" placeholder="password" onChange={onChangeHandler}/>
            <button>Login</button>
        </form>
        </div>
    )
}

export default Login