const API_URL = 'http://127.0.0.1:8000/api/personas/'

export const listPersonas = async () => {
    return await fetch(API_URL);
}