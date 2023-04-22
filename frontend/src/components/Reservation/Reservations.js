import { useContext, useEffect, useState } from "react"
import { AuthContext } from "../../context/AuthContext"
import { getAllReservations } from "../../services/reservationRequests"
import styles from "./Reservations.module.css"

const Reservations = () => {
    const { user } = useContext(AuthContext)
    const [reservations, setReservations] = useState([])

    useEffect(() => {
        getAllReservations()
            .then(result => {
                setReservations(result)
            })
    }, [reservations.length])

    return (
        <div className={styles.reservations}>
            {reservations.length > 0
                ? <>{
                    user.role === 'admin'
                        ? reservations.map(r =>
                            <section>
                                <h3>Reservation ID: {r.id}</h3>
                                <h3>User ID: {r.user_id}</h3>
                                <h3>Hotel ID: {r.hotel_id}</h3>
                                <h3>Nights: {r.nights}</h3>
                                <h3>Status: {r.status}</h3>
                                <h3>Created On: {new Date(r.created_on).toLocaleDateString()}</h3>
                            </section>
                        )
                        : <h1>You have no access to this page</h1>
                }</>
                : <h1>No reservations :(</h1>
            }
        </div>
    )
}

export default Reservations