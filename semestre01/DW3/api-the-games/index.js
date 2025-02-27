import express from "express";
import mongoose from "mongoose";
import Games from "./models/games.js";
const app = express();

// Configuração do express
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// Iniciando a conexão com o banco de dados do MongoDB
mongoose.connect("mongodb://127.0.0.1:27017/api-the-games");

// Rota principal
app.get("/", (req, res) => {
  res.send("API iniciada com sucesso!");
});

// Iniciar o servidor
const port = 4000;
app.listen(port, (error) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`API rodando em http://localhost:${port}`);
  }
});
