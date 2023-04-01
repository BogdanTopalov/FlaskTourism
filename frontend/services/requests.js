const apiUrl = 'http://127.0.0.1:5000'

async function request(url) {
    const response = await fetch(url)
    const result = await response.json()

    return result
}
