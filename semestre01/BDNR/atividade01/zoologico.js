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
    const database = client.db("zoo_db");
    // selecionar a coleção "animais"
    const animais = database.collection("animais");

    // Limpa a coleção antes de inserir novos dados
    await animais.deleteMany({});

    // inserindo dados no banco
    await animais.insertMany([
      {
        nome: "Thor",
        especie: "Tigre-de-bengala",
        idade: 4,
        dieta: "Carnívoro",
        habitat: "Floresta Tropical",
        vacinado: false,
      },
      {
        nome: "Luna",
        especie: "Arara-azul",
        idade: 2,
        dieta: "Herbívoro",
        habitat: "Floresta Tropical",
        vacinado: false,
      },
      {
        nome: "Rex",
        especie: "Leão",
        idade: 5,
        dieta: "Carnívoro",
        habitat: "Savanas Africanas",
        vacinado: false,
      },
      {
        nome: "Simba",
        especie: "Leão",
        idade: 6,
        dieta: "Carnívoro",
        habitat: "Deserto",
        vacinado: false,
      },
      {
        nome: "Kiara",
        especie: "Elefante-africano",
        idade: 16,
        dieta: "Herbívoro",
        habitat: "Savanas Africanas",
        vacinado: false,
      },
      {
        nome: "Balu",
        especie: "Urso-pardo",
        idade: 7,
        dieta: "Onívoro",
        habitat: "Florestas Temperadas",
        vacinado: false,
      },
    ]);

    // CONSULTAS
    // listar todos os animais herbívoros
    const herbivoros = await animais.find({ dieta: "Herbívoro" }).toArray();
    console.log("Herbívoros: ", herbivoros);

    // listar os animais que vivem em deserto
    const deserto = await animais.find({ habitat: "Deserto" }).toArray();
    console.log("Habitat deserto: ", deserto);

    // ATUALIZAÇÃO DE DADOS
    await animais.updateMany(
      { especie: "Leão" }, // filtro para encontrar os leões
      { $set: { felinos: true } } // adiciona o campo 'felinos' com valor true
    );

    // atualizar o campo 'felinos' como false para os outros animais
    await animais.updateMany(
      { especie: { $ne: "Leão" } }, // ailtro para encontrar animais que não são leões
      { $set: { felinos: false } } // adiciona o campo 'felinos' com valor false
    );

    // vacinar os felinos
    await animais.updateMany({ felinos: true }, { $set: { vacinado: true } });
    const vacinados = await animais.find({ vacinado: true }).toArray();
    console.log("Animais vacinados:", vacinados);

    // EXCLUSÃO
    // exluir do banco os animais idosos
    const idosos = await animais.deleteMany({ idade: { $gt: 15 } });
    console.log("Os idosos morreram:", idosos)

    // ADICIONANDO UM CUIDADOR PARA CADA ANIMAL PELO NOME DELE
    await animais.updateOne(
      { nome: "Thor" },
      { $set: { cuidador: "Giovana" } }
    );
    await animais.updateOne(
      { nome: "Luna" },
      { $set: { cuidador: "Manuela" } }
    );
    await animais.updateOne({ nome: "Rex" }, { $set: { cuidador: "Mariana" } });
    await animais.updateOne(
      { nome: "Simba" },
      { $set: { cuidador: "Leandro" } }
    );
    await animais.updateOne(
      { nome: "Kiara" },
      { $set: { cuidador: "Amanda" } }
    );
    await animais.updateOne({ nome: "Balu" }, { $set: { cuidador: "Arthur" } })

    // LISTAR OS ANIMAIS QUE AINDA ESTÃO VIVOS; LISTAR OS ANIMAIS COM SEUS RESPECTIVOS CUIDADORES;
    const cuidadores = await animais.find({}).toArray();
    console.log("Animais vivos:", cuidadores);

  } finally {
    await client.close();
  }
}
main().catch(console.error);

/*
Para rodar a aplicação:
1. npm init -y 
2. npm install mongodb 
3. Navegar até a pasta onde o arquivo se encontra
4. node zoologico.js
*/
