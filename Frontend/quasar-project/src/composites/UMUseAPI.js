import { api } from "src/boot/axios";

export default function UseApi(url) {
 const listUM = async () => {
    try {
        const data = await api.get(url)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const postUM = async (form) => {
    try {
        const data = await api.post(url,form)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const updateUM = async (form) => {
    try {
        const data = await api.put(`${url}${form.id}`,form)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const removeUM = async (id) => {
    try {
        const data = await api.delete(`${url}${id}/`)
        return data
    } catch (error) {
        alert(error)
    }
 }    
 return{
    listUM,
    postUM,
    updateUM,
    removeUM,
 }   
}