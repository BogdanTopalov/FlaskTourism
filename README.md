# FlaskTourism
 
### How to start the project
1. Clone Repo
2. ```pip install -r requirements.txt``` in the backend folder to install needed packages
3. ```flask run``` in the backend folder terminal to run the backend server locally on *http://127.0.0.1:5000/*
4. ```npm start``` in the frontend folder terminal to run the frontend server locally on *http://localhost:3000*
5. Explore the project on *http://localhost:3000*

### API Endpoints
- /register
  * Request: `{"first_name": "...", "last_name": "...", "email": "...", "password": "..."}`
  * Response: `{"token": "..."}`
- /login
  * Request: `{"email": "...", "password": "..."}`
  * Response: `{"token": "..."}`
- /user
  * Request: `{"token": "..."}`
  * Response: `{"id": , "email": "...", "first_name": "...", "last_name": "...", "role": "..."}`
- /hotels
  * Request: `no body`
  * Response: List of dictionaries 
    ```
    [{
        "country": "...",
        "id": ...,
        "city": "...",
        "price_per_night": ...,
        "image_url": "...",
        "stars": ...,
        "name": "..."
    }, ...]
    ```
- /hotels/add
  * Request: 
    ```
    {
      "country": "...",
      "name": "...",
      "stars": ...,
      "price_per_night": ..., 
      "city": "...",
      "image_url": "..."
    }
    ```
  * Response: `same as Request`
- /hotels/:id
  * Request: `no body`
  * Response: 
    ```
    {
      "country": "...",
      "name": "...",
      "stars": ...,
      "price_per_night": ..., 
      "city": "...",
      "image_url": "..."
    }
    ```
- /hotels/update/:id
  * Request:
    ```
    {
      "country": "...",
      "name": "...",
      "stars": ...,
      "price_per_night": ..., 
      "city": "...",
      "image_url": "..."
    }
    ```
  * Response:
    ```
    {
      "country": "...",
      "name": "...",
      "stars": ...,
      "price_per_night": ..., 
      "city": "...",
      "image_url": "..."
    }
    ```
- /hotels/delete/:id
  * Request: `no body`
  * Response: `{"message": "Hotel deleted successfully"}`
- /reservations
  * Request: `no body`
  * Response: List of dictionaries
    ```
    [{
        "created_on": "...",
        "id": ...,
        "hotel_id": ...,
        "user_id": ...,
        "nights": ...,
        "status": "..."
    }, ...]
    ```
- /reservations/create
  * Request:
    ```
    {
      "hotel_id": ...,
      "nights": ...
    }
    ```
  * Response:
    ```
    {
      "clientSecret": "...",
      "reservation_id": ...
    }
    ```
- /reservations/update/:id
  * Request: `no body`
  * Response: `{"message": "Reservation updated successfully"}`
