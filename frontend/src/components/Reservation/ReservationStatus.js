import { useParams } from "react-router-dom"
import { updateReservation } from "../../services/reservationRequests"
import styles from "./ReservationStatus.module.css"

const ReservationStatus = () => {
    const queryParameters = new URLSearchParams(window.location.search)
    const paymentStatus = queryParameters.get("redirect_status")
    const {reservation_id} = useParams()
    
    if (paymentStatus === 'succeeded') {
        updateReservation(reservation_id).then()
    }

    return (
        <div className={styles.status}>
            {paymentStatus === 'succeeded'
                ? <h1>Reservation Completed</h1>
                : <h1>Reservation Cenceled</h1>
            }
        </div>
    )
}

export default ReservationStatus