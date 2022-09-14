import { api } from "src/boot/axios";

export default function UseApi(url) {
 const listGame = async () => {
    try {
        const data = await api.get(url)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const postGame = async (form) => {
    try {
        const data = await api.post(url,form)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const updateGame = async (form) => {
    try {
        const data = await api.put(`${url}${form.id}`,form)
        return data
    } catch (error) {
        throw new Error(error)
    }
 }
 const removeGame = async (id) => {
    try {
        const data = await api.delete(`${url}${id}/`)
        return data
    } catch (error) {
        alert(error)
    }
 }    
 return{
    listGame,
    postGame,
    updateGame,
    removeGame,
 }   
}