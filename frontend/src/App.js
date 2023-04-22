import { loadStripe } from '@stripe/stripe-js';
import { Route, Routes } from 'react-router-dom';
import './App.css';
import Home from './components/Home/Home';
import AddHotel from './components/Hotels/AddHotel';
import HotelDetails from './components/Hotels/HotelDetails';
import Hotels from './components/Hotels/Hotels';
import Login from './components/Login/Login';
import Logout from './components/Logout/Logout';
import Navigation from './components/Navigation/Navigation';
import Register from './components/Register/Register';
import Reservation from './components/Reservation/Reservation';
import ReservationStatus from './components/Reservation/ReservationStatus';
import Reservations from './components/Reservation/Reservations';
import { AuthProvider } from './context/AuthContext';


export const stripePromise = loadStripe(`${process.env.REACT_APP_STRIPE_PK}`)


function App() {
	return (
		<AuthProvider>
			<Navigation />
			<Routes>
				<Route path='/' element={<Home />} />
				<Route path='/register' element={<Register />} />
				<Route path='/login' element={<Login />} />
				<Route path='/logout' element={<Logout />} />
				<Route path='/hotels' element={<Hotels />} />
				<Route path='/hotels/:hotel_id' element={<HotelDetails />} />
				<Route path='/add/hotel' element={<AddHotel />} />
				<Route path='/reservation' element={<Reservation />} />
				<Route path='/reservations' element={<Reservations />} />
				<Route path='/reservations/status/:reservation_id' element={<ReservationStatus />} />
			</Routes>
		</AuthProvider>
	);
}

export default App;
