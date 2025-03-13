import Game from "../models/Games.js";

class gameService {
  // Função para listar jogos
  async getAll() {
    try {
      const games = await Game.find();
      return games;
    } catch (error) {
      console.log(error);
    }
  }
  // Função para cadastrar jogos
  async Create(title, plataform, year, price) {
    try {
      const newGame = new Game({
        // title: title, é a mesma coisa que:
        // Isso se chama desestruturação
        title,
        plataform,
        year,
        price,
      });
      // Método do mongoose pra cadastrar algo; tenho que esperar ele terminar de cadastrar para continuar
      await newGame.save();
    } catch (error) {
      console.log(error);
    }
  }

  //Função para deletar um jogo
  async Delete(id) {
    try {
      await Game.findByIdAndDelete(id);
      console.log(`Game com a id: ${id} foi excluído.`);
    } catch (error) {
      console.log(error);
    }
  }

  // Função para alterar jogos
  async Update(id, title, plataform, year, price) {
    try {
      await Game.findByIdAndUpdate(id, {
        title,
        plataform,
        year,
        price,
      });
      console.log(`Dados do game com a id: {id} alterados com sucesso!`);
    } catch (error) {
      console.log(error);
    }
  }
}
export default new gameService();
