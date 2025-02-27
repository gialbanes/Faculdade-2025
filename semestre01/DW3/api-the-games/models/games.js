import mongoose from "mongoose";

// Schema são os atributos que ele vai ter
const gamesSchema = new mongoose.Schema({
  title: String,
  plataform: String,
  year: Number,
  price: Number,
});

// Aqui está sendo criada a coleção games no banco de dados
// Game é o nome da coleção, mas no BD o mongoose vai criar "games" por padrão, já que é uma coleção
const Games = mongoose.model("Game", gamesSchema);

export default Games;
