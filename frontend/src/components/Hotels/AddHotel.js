import { useState } from "react"
import { addHotel } from "../../services/hotelRequests"
import { useNavigate } from "react-router-dom"
import styles from "./AddHotel.module.css"

const AddHotel = () => {
    const [formValues, setFormValues] = useState({})
    const navigate = useNavigate()

    const onChangeHandler = (e) => {
        const { name, value } = e.target
        setFormValues(
            { ...formValues, [name]: value }
        )
    }

    const onSubmitHandler = (e) => {
        e.preventDefault()

        addHotel(
            formValues.name,
            Number(formValues.stars),
            formValues.country,
            formValues.city,
            formValues.image_url,
            Number(formValues.price_per_night)
        ).then(result => {
            navigate(`/hotels/${result.id}`)
        })
    }

    return (
        <div className={styles.add}>
            <form onSubmit={onSubmitHandler}>
                <input type='text' name='name' placeholder="Hotel Name" required onChange={onChangeHandler} />
                <input type='text' name='stars' placeholder="Stars" required onChange={onChangeHandler} />
                <input type='text' name='country' placeholder="Country" required onChange={onChangeHandler} />
                <input type='text' name='city' placeholder="City" required onChange={onChangeHandler} />
                <input type='text' name='image_url' placeholder="Image URL" required onChange={onChangeHandler} />
                <input type='text' name='price_per_night' placeholder="Price Per Night" required onChange={onChangeHandler} />
                <button>Add</button>
            </form>
        </div>
    )
}

export default AddHotel