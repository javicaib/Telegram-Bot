import { api } from "src/boot/axios";

export default function UseApi(url) {
 const listPlataform = async () => {
    try {
        const data = await api.get(url)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const postPlataform = async (form) => {
    try {
        const data = await api.post(url,form)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const updatePlataform = async (form) => {
    try {
        const data = await api.put(`${url}${form.id}`,form)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const removePlataform = async (id) => {
    try {
        const data = await api.delete(`${url}${id}/`)
        return data
    } catch (error) {
        alert(error)
    }
 }    
 return{
    listPlataform,
    postPlataform,
    updatePlataform,
    removePlataform,
 }   
}