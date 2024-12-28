import axios from "axios";

// Base API URL
const API_URL = "https://fullstackproject1-56jm.onrender.com/api/elements";

// Fetch elements with optional filters
export const getElements = async (filters = {}) => {
  const { data } = await axios.get(API_URL, { params: filters });
  return data;
};

// Add a new element
export const addElement = async (element) => {
  const { data } = await axios.post(API_URL, element);
  return data;
};

// Edit an existing element by ID
export const editElement = async (id, element) => {
  const { data } = await axios.put(`${API_URL}/${id}`, element);
  return data;
};

// Delete an element by ID
export const deleteElement = async (id) => {
  await axios.delete(`${API_URL}/${id}`);
};
