import UseApi from "src/composites/GameUseAPI";
export default function gameService(params) {

    const {listGame,postGame,updateGame,removeGame} = UseApi('game/')
    return {listGame,
            postGame,
            updateGame,
            removeGame
           }
    
}