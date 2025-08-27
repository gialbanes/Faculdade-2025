<?php
// carrega as bibliotecas do firebase 
// o DIR é p não ter problemas depois; é uma superclasse; concateno de onde estou até a pasta
require_once __DIR__.'/vendor/autoload.php';

use Kreait\Firebase\Factory;

// criar como se fosse a conexão com o BD(constructor), iniciar, e criar as funções
class FirebaseCRUD{
    private $database; //variável

    public function __construct(){ // conexão 
        $firebase = (new Factory)
        ->withServiceAccount(__DIR__.'/assets/config/chave.json') // local da minha chave
        ->withDataBaseUri('https://biblioteca-dsm3-771b0-default-rtdb.firebaseio.com/') // URL do meu BD no firebase 
        ->createDatabase();

        // inicializar a conexão com o banco de dados 
        // o this chama a veriável private 
        $this->database = $firebase;
    }
    // inserir dados (create)
    public function create($livro){
        // a var ref busca a minha coleção livros dentro do banco; caso eu nã tenha a coleção, ele cria
        $ref = $this->database->getReference('livros'); 
        // envia as infos do parâmetro p banco 
        $ref->push($livro);
    }

    // consultar todos os documentos (read)
    // sem parâmetro pq pega as infos do banco 
    public function read(){
        $ref = $this->database->getReference('livros');
        // pega oq foi coletado na variável livros e depois retorna
        $livros = $ref->getValue();
        return $livros;
    }

    // atualizar um documento (update)
    public function update($id, $livro){
        $ref = $this->database->getReference('livros/'.$id);
        // faz a alteração no livro específico
        $ref->set($livro);
    }

    // excluir um documento (delete)
    public function delete($id){
        $ref = $this->database->getReference('livros/'.$id);
        // pega o livro em específico e remove 
        $ref->remove();
    }
}
// testando as funções CRUD 
// instanciando um objeto 
$firebaseCrud = new FirebaseCRUD();

// inserir um livro no banco 
$firebaseCrud->create([
    'titulo' => 'O Senhor dos Anéis',
    'autor' => 'J. R. R. Tolkien',
    'genero' => 'Fantasia'
]);
?>