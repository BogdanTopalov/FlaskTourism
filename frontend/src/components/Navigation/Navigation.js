import { useContext } from "react"
import { Link } from "react-router-dom"
import { AuthContext } from "../../context/AuthContext"
import styles from "./Navigation.module.css"


const TopNavigation = () => {
    const { user, isAuthenticated } = useContext(AuthContext)

    return (
        <>
            {user.role === 'admin'
                ? <div className={styles.reservations}>
                    <Link to='/reservations'>Reservations</Link>
                </div>
                : <></>
            }

            <div className={styles.top}>
                <Link to='/hotels'>Hotels</Link>
                {isAuthenticated
                    ? <div>
                        <p> {user.email}</p>
                        <Link to='/logout'>Logout</Link>
                    </div>
                    : <div className={styles.loginRegister}>
                        <Link to='/login' >Login</Link>
                        <Link to='/register' >Register</Link>
                    </div>
                }
            </div>
        </>
    )
}

export default TopNavigation