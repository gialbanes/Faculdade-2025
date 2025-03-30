import express from "express";
const app = express();
import livroRoutes from "./routes/livroRoutes.js";
import Livro from "./models/Livros.js";
import mongoose from './config/db-connection.js';

app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use("/", livroRoutes);

//mongoose.connect("mongodb://127.0.0.1:27017/api-livros");

const port = 4000;
app.listen(port, (error) => {
  if (error) {
    console.log("error");
  }
  console.log(`API rodando em http://localhost:${port}`);
});
