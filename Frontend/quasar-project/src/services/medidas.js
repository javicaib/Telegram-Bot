import UseApi from "src/composites/UMUseAPI";

export default function umformService(params) {

    const {listUM,postUM,updateUM,removeUM} = UseApi('mesure-unit/')
    return {listUM,
            postUM,
            updateUM,
            removeUM
           }
    
}