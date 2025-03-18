import mongoose from "mongoose";

// Documento aninhado, primeiro crio o documento que vai estar aninhado, e depois o que vai receber ele
const descriptionSchema = new mongoose.Schema({
  genre: String,
  plataform: String,
  rating: String,
});

const gameSchema = new mongoose.Schema({
  title: String,
  year: Number,
  price: Number,
  descriptions: [descriptionSchema] // Array de objetos, se não precisar só tirar os colchetes
});

// Aqui está sendo criado a coleção games no banco de dados
const Game = mongoose.model("Game", gameSchema);

export default Game;