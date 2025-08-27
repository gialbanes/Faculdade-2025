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
  async Create(title, year, price, descriptions) {
    try {
      const newGame = new Game({
        // title: title, é a mesma coisa que:
        // Isso se chama desestruturação
        title,
        year,
        price,
        descriptions,
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
  async Update(id, title, year, price, descriptions) {
    try {
      await Game.findByIdAndUpdate(id, {
        title,
        year,
        price,
        descriptions,
      });
      console.log(`Dados do game com a id: {id} alterados com sucesso!`);
    } catch (error) {
      console.log(error);
    }
  }

  // Função para listar um único jogo
  async getOne(id) {
    try {
      const game = await Game.findOneAndDelete({_id:id}) // o primeiro é o id do BD e o outro oq eu vou enviar 
      return game;
    } catch (error) {
      console.log(error);
    }
  }
}
export default new gameService();
