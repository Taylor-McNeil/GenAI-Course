import axios from "axios";

// Define the backend URL (replace with your actual backend URL)
const BASE_URL = "http://127.0.0.1:8000"; // Backend FastAPI URL

// Function to fetch words from the backend
export const getAllWords = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/api/words/`);
    return response.data; // Return words data
  } catch (error) {
    console.error("Error fetching words:", error);
    return []; // Return empty array if there's an error
  }
};
