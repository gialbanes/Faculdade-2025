import express from "express";
const gameRoutes = express.Router();
import gameController from "../controllers/gameController.js";

// Endpoint para listar todos os games
gameRoutes.get("/games", gameController.getAllGames);

// Endpoint para cadastrar um novo game
// Nâo tem problema ser a mesma rota, pois os métodos são diferentes; É uma boa prática a rota ser igual
gameRoutes.post("/games", gameController.createGame);

// Endpoint para deletar um game
gameRoutes.delete("/games/:id", gameController.deleteGame);

// Endpoint para alterar um game
gameRoutes.put("/games/:id", gameController.updateGame);

// Endpoint para listar um único jogo
gameRoutes.get("/games/:id", gameController.getOneGame)
export default gameRoutes;
