import UseApi from "src/composites/PlataformUseAPI";
export default function plataformService(params) {

    const {listPlataform,postPlataform,updatePlataform,removePlataform} = UseApi('plataform/')
    return {listPlataform,
            postPlataform,
            updatePlataform,
            removePlataform
           }
    
}
