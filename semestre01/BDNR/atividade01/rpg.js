// importando o módulo MongoClient
const { MongoClient } = require("mongodb");

// função principal
async function main() {
  // definir a uri de conexão com o MongoDB
  const uri = "mongodb://127.0.0.1:27017";
  // criar uma instância do MongoClient
  const client = new MongoClient(uri);

  try {
    // connect com o servidor mongodb
    await client.connect();
    // selecionar o banco de dados
    const database = client.db("rpg_db");
    // selecionar a coleção "animais"
    const personagens = database.collection("personagens");

    // Limpa a coleção antes de inserir novos dados
    await personagens.deleteMany({});

    await personagens.insertMany([
        {
          nome: "Arya Ventis",
          classe: "mago",
          nivel: 18,
          habilidades: ["soco de trovão", "invisibilidade"],
          vida: 150,
        },
        {
          nome: "Borin Pedraqueixo",
          classe: "guerreiro",
          nivel: 12,
          habilidades: ["golpe de espada", "escudo impenetrável"],
          vida: 120,
        },
        {
          nome: "Lia Sombria",
          classe: "arqueiro",
          nivel: 14,
          habilidades: ["tiro certeiro", "camuflagem"],
          vida: 100,
        },
        {
          nome: "Karn Lançaferro",
          classe: "guerreiro",
          nivel: 8,
          habilidades: ["golpe mortal", "raiva incontrolável"],
          vida: 80,
        },
        {
          nome: "Thalia Luz do Norte",
          classe: "mago",
          nivel: 20,
          habilidades: ["mago do gelo", "cura divina"],
          vida: 180,
        },
        {
          nome: "Zack Mão de Ferro",
          classe: "guerreiro",
          nivel: 15,
          habilidades: ["golpe pesado", "defesa férrea"],
          vida: 90,
        }
    ]);

    // CONSULTAS DO REINO 
    // personagens de nível superior a 10 
    const personagensNivelSuperior10 = await personagens.find({ nivel: { $gt: 10 } }).toArray();
    console.log("Personagens de nível superior a 10:", personagensNivelSuperior10);

    // guerreiros disponíveis para a missão 
    const guerreirosDisponiveis = await personagens.find({ classe: "guerreiro", vida: { $gt: 0 } }).toArray();
    console.log("Guerreiros disponíveis para missão urgente:", guerreirosDisponiveis);

    // MELHORIAS E PERDAS
    // aumentando a vida de todos os guerreiros para 200
    await personagens.updateMany(
        { classe: "guerreiro" },
        { $set: { vida: 200 } }
      );
      // listando os guerreiros que receberam vida 
      const treinamento = await personagens.find({ classe: "guerreiro", vida: 200 }).toArray();
      console.log("Guerreiros que receberam treinamento especial:", treinamento);

      // guerreiros com vida menor que 30 foram derrotados em uma batalha 
      await personagens.deleteMany({ vida: { $lt: 30 } });
      // listando os guerreiros que receberam vida 
      const derrotados = await personagens.find({vida: {$lt:30} }).toArray();
      console.log("Guerreiros que foram derrotados na batalha:", derrotados);

  } finally{
    await client.close();
  }
}
main().catch(console.error);

/*
Para rodar a aplicação:
1. npm init -y 
2. npm install mongodb 
3. Navegar até a pasta onde o arquivo se encontra
4. node rpg.js
*/