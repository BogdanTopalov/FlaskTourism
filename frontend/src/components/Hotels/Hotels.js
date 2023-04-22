import { useContext, useEffect, useState } from "react"
import { getAllHotels } from "../../services/hotelRequests"
import { Link, useNavigate } from "react-router-dom"
import { AuthContext } from "../../context/AuthContext"
import styles from "./Hotels.module.css"

const Hotels = () => {
    const { user } = useContext(AuthContext)
    const [hotels, setHotels] = useState([])
    const navigate = useNavigate()

    useEffect(() => {
        getAllHotels()
            .then(result => {
                setHotels(result)
            })
    }, [hotels.length])

    const onAddHandler = () => {
        navigate(`/add/hotel`)
    }

    return (
        <div className={styles.hotels}>
            {hotels.length > 0
                ? hotels.map(h =>
                    <section
                        key={h.id}
                        style={{
                            backgroundImage: `url("${h.image_url}")`, 
                            backgroundPosition: 'center',
                            backgroundSize: 'cover'
                        }}>
                        <h2>{h.name}</h2>
                        <Link to={`/hotels/${h.id}`}>View</Link>
                    </section>
                )
                : <h1>No hotels available :(</h1>
            }

            {user.role === 'admin'
                ? <button onClick={onAddHandler}>Add Hotel</button>
                : <></>
            }
        </div>
    )
}

export default Hotels
