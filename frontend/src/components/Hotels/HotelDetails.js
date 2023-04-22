import { useContext, useEffect, useState } from "react"
import { deleteHotel, getSingleHotel, updateHotel } from "../../services/hotelRequests"
import { useNavigate, useParams } from "react-router-dom"
import { AuthContext } from "../../context/AuthContext";
import styles from "./HotelDetails.module.css"

const HotelDetails = () => {
    const date = new Date();
    const today = date.toJSON().slice(0, 10)

    const { user } = useContext(AuthContext)
    const { hotel_id } = useParams()
    const [hotel, setHotel] = useState({})
    const [formValues, setFormValues] = useState({})
    const navigate = useNavigate()

    useEffect(() => {
        getSingleHotel(hotel_id)
            .then(result => {
                setHotel(result)
                setFormValues(result)
            })
    }, [hotel_id])

    const onChangeHandler = (e) => {
        const { name, value } = e.target
        setFormValues(
            { ...formValues, [name]: value }
        )
    }

    const onSubmitHandler = (e) => {
        e.preventDefault()

        const date_from = new Date(formValues.from)
        const date_to = new Date(formValues.to)

        const nights = (date_to.getTime() - date_from.getTime()) / (1000 * 3600 * 24) + 1

        navigate('/reservation', { state: { nights, pricePerNight: hotel.price_per_night, hotel_id } })
    }

    const onUpdateHandler = (e) => {
        e.preventDefault()

        updateHotel(
            hotel_id,
            formValues.name,
            Number(formValues.stars),
            formValues.country,
            formValues.city,
            formValues.image_url,
            Number(formValues.price_per_night)
        ).then(
            navigate(`/hotels`)
        )
    }

    const onDeleteHandler = () => {
        const confirm = window.confirm('Do you want to delete this hotel?')

        if (confirm) {
            deleteHotel(hotel_id)
            navigate('/hotels')
        }
    }

    return (
        <div className={styles.details}>

            <img src={hotel.image_url} alt="hotel" />
            <div>
                <h1>{hotel.name}</h1>
                <h2>{hotel.stars} &#9733;</h2>
                <h3>{hotel.country}</h3>
                <h3>{hotel.city}</h3>
                <h2>{hotel.price_per_night} BGN /Night</h2>
            </div>

            <form onSubmit={onSubmitHandler} className={styles.form}>
                <label>From: </label>
                <input
                    type='date'
                    name='from'
                    min={today}
                    required
                    onChange={onChangeHandler}
                />
                <label>To: </label>
                <input
                    type='date'
                    name='to'
                    min={formValues.from}
                    required
                    onChange={onChangeHandler}
                />
                <button>Reserve</button>
            </form>

            {user.role === 'admin'
                ? <div>
                    <form onSubmit={onUpdateHandler} className={styles.form}>
                        <input type='text' name='name' placeholder={hotel.name} value={formValues.name} onChange={onChangeHandler} required />
                        <input type='text' name='stars' placeholder={hotel.stars} value={formValues.stars} onChange={onChangeHandler} required />
                        <input type='text' name='country' placeholder={hotel.country} value={formValues.country} onChange={onChangeHandler} required />
                        <input type='text' name='city' placeholder={hotel.city} value={formValues.city} onChange={onChangeHandler} required />
                        <input type='text' name='image_url' placeholder={hotel.image_url} value={formValues.image_url} onChange={onChangeHandler} required />
                        <input type='text' name='price_per_night' placeholder={hotel.price_per_night} value={formValues.price_per_night} onChange={onChangeHandler} required />
                        <button>Update</button>
                    </form>
                    <button onClick={onDeleteHandler}>Delete</button>
                </div>
                : <></>
            }
        </div>
    )
}

export default HotelDetails
