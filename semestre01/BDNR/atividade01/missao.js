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
    const database = client.db("space_db");
    // selecionar a coleção "animais"
    const naves = database.collection("naves");
    // selecionar a coleção tripulantes como parte do desafio 
    const tripulantes = database.collection("tripulantes");


    // limpa as coleções antes de inserir novos dados
    await naves.deleteMany({});
    await tripulantes.deleteMany({});

    // inserindo as naves
    const navesDados = await naves.insertMany([
      {
        nome: "Estrela Cadente",
        tipo: "Exploração",
        capacidade: 2,
        emMissao: false,
      },
      {
        nome: "Colossus",
        tipo: "Carga",
        capacidade: 4,
        emMissao: false,
      },
      {
        nome: "Fênix",
        tipo: "Combate",
        capacidade: 3,
        emMissao: true,
      },
      {
        nome: "Voyager",
        tipo: "Exploração",
        capacidade: 6,
        emMissao: true,
      },
    ]);

    // inserindo os dados de tripulante na coleção
    const tripulantesDados = [
        {
          nome: "Giovana",
          cargo: "Capitã",
          nave_id: navesDados.insertedIds[0], // tripulante da primeira nave - Estrela Cadente
        },
        {
          nome: "Manuela",
          cargo: "Engenheira",
          nave_id: navesDados.insertedIds[1], // tripulante da primeira nave - Colossus
        },
        {
          nome: "Mariana",
          cargo: "Comandante",
          nave_id: navesDados.insertedIds[2], // tripulante da primeira nave - Fênix
        },
        {
          nome: "Leandro",
          cargo: "Técnico",
          nave_id: navesDados.insertedIds[3], // tripulante da primeira nave - Voyager
        },
      ];
  
      // inserindo os tripulantes em cada uma das naves com base no ID da nave
      await tripulantes.insertMany(tripulantesDados);

    // LISTAR OS TRIPULANTES
    const todosTripulantes = await tripulantes.find().toArray();
    console.log("Tripulantes:", todosTripulantes);

    // CONSULTAS ESTRATÉGICAS
    // naves que estão em missão
    const missao = await naves.find({ emMissao: true }).toArray();
    console.log("Naves em missão:", missao);

    // naves com mais de de 5 tripulantes
    const capMax = await naves.find({ capacidade: { $gt: 5 } }).toArray();
    console.log("Naves com capacidade maior que 5 tripulantes:", capMax);

    // ATUALIZAÇÕES DE FROTA
    // naves do tipo 'Carga' vão ser desativadas
    await naves.updateMany(
        { tipo: "Carga" },
        { $set: { emMissao: false } }
    );
    
    // listar as desativadas
    const desativadas = await naves.find({ tipo: "Carga", emMissao: false }).toArray();
    console.log("Nave(s) desativada(s):", desativadas);

    // DESCOMISSIONAMENTO
    // naves que tem capacidade menor que 3 tripulantes são obsoletas
    const obsoletas = await naves.find({ capacidade: { $lt: 3 } }).toArray(); // pegando as naves com capacidade menor que 3 tripulantes
    await naves.deleteMany({ capacidade: { $lt: 3 } }); // excluindo estas naves
    console.log("Nave(s) obsoleta(s):", obsoletas); //listando as naves removidas

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
4. node missao.js
*/
