// importar o módulo MongoClient 
const {MongoClient} = require('mongodb');

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
        const database = client.db('biblioteca');
        // selecionar a coleção "livros"
        const livros = database.collection('livros');

        // inserindo dados no bd
        await livros.insertMany([
            {titulo: 'Dom Casmurro', autor: 'Machado de Assis', ano : 1899, genero : 'Romance'},
            {titulo: 'Memórias Póstumas de Brás Cubas', autor: 'Machado de Assis', ano : 1881, genero : 'Romance'},
            {titulo: 'O Alienista', ano : 1882, autor: 'Machado de Assis', genero : 'Conto'}
        ]);
    }finally{
        await client.close();
    }
}

// chama a função principal e captura o erro, se houver 
main().catch(console.error);
