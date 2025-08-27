const mongoose = require("mongoose");

// Conexão BD
mongoose.connect("mongodb://localhost:27017/receitasDB", {
  userNewUrlParser: true,
  useUnifiedTopology: true,
});

//Lista de receita para inserir
const receitas = [
  {
    nome: "Bolo de chocolate",
    ingredientes: ["Farinha", "Acucar", "Ovos", "Chocolate em pó", "Fermento"],
    instrucoes: "Misture todos os ingredientes e asse por 40 minutos",
  },
  // próximas receitas se precisar inserir via script
];

// inserir receitas no banco de dados
async function inserirReceitas() {
  try {
    await Receita.deleteMany({}); // limpa a coleção antes de inserir
    await Receita.insertMany(receitas);
    console.log("Receita inserida com sucesso!");
    mongoose.connect.close();
  } catch (error) {
    console.log(`Erro ao inserir receita: ${error}`);
    mongoose.connect.close();
  }
}

inserirReceitas();
