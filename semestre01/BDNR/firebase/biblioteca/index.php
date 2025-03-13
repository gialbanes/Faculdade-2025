<?php
require_once 'vendor/autoload.php';

use Kreait\firebase\Factory;

class FirebaseCRUD{
    private $database;

    public function __construct(){
        $firebase = (new Factory)
        ->withServiceAccount(__DIR__.'/chave.json')
        ->withDataBaseUri('https://biblioteca-dsm3-771b0-default-rtdb.firebaseio.com/')
        ->createDatabase();

        // inicializar a conexão com o banco de dados 
        $this->database = $firebase;
    }

    /*
    // inserir dados (create)
    public function create($livro){
        $ref = $this->database->getReference('livros');
        $ref->push($livro);
    }

    // consultar todos os documentos (read)
    public function read(){
        $ref = $this->database->getReference('livros');
        $value = $ref->getValue();
    }

    // atualizar um documento (update)
    public function update($id, $livro){
        $ref = $this->database->getReference('livros/'.$id);
        $ref->set($livro);
    }

    // excluir um documento (delete)
    public function delete($id){
        $ref = $this->database->getReference('livros/'.$id);
        $ref->remove();
    }
    */
}
// testando as funções CRUD 
$firebaseCrud = new FirebaseCRUD();
$firebaseCrud->create([
    'titulo' => 'O Senhor dos Anéis',
    'autor' => 'J. R. R. Tolkien',
    'genero' => 'Fantasia'
]);
?>


