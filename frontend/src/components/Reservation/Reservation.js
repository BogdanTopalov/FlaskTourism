import { Elements } from "@stripe/react-stripe-js";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { stripePromise } from "../../App.js";
import { createReservation } from "../../services/reservationRequests";
import CheckoutForm from "./CheckoutForm";


const Reservation = () => {
    const [clientSecret, setClientSecret] = useState("");
    const [reservationId, setReservationId] = useState("")
    const { state } = useLocation()

    useEffect(() => {
        createReservation(state.hotel_id, state.nights)
            .then(data => {
                setClientSecret(data.clientSecret)
                setReservationId(data.reservation_id)
            })
    }, [state.hotel_id, state.nights])

    const appearance = {
        theme: 'stripe',
    }

    const options = {
        clientSecret,
        appearance,
    }

    return (
        <div className="App">
            {clientSecret && (
                <Elements options={options} stripe={stripePromise}>
                    <CheckoutForm pricePerNight={state.pricePerNight} nights={state.nights} reservationId={reservationId}/>
                </Elements>
            )}
        </div>
    )
}

export default Reservation