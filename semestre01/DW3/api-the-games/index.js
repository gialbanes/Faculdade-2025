import express from "express";
const app = express();
//criando uma variavel pro express

//configuracao do express
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

//ROTA PRINCIPAL
app.get("/", (req, res) => {
  //   res.send("API iniciada com sucesso!");
  const games = [
    {
      tittle: "Game 1",
      year: 2020,
      platform: "PC",
      price: 20.99,
    },
    {
      tittle: "Game 2",
      year: 2023,
      platform: "Mobile",
      price: 4.5,
    },
  ];
  res.json(games) //enviando os dados em json 
});

//iniciar servidor
const port = 4000;
//criando variavel para a porta
app.listen(port, (error) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`API rodando em http://localhost:${port}.`);
  }
});