import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/elements";

export const getElements = async (filters = {}) => {
    const { data } = await axios.get(API_URL, { params: filters });
    return data;
  };
  

export const addElement = async (element) => {
  const { data } = await axios.post(API_URL, element);
  return data;
};

export const editElement = async (id, element) => {
  const { data } = await axios.put(`${API_URL}/${id}`, element);
  return data;
};

export const deleteElement = async (id) => {
  await axios.delete(`${API_URL}/${id}`);
};
