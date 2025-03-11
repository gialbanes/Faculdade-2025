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
export default gameRoutes;
