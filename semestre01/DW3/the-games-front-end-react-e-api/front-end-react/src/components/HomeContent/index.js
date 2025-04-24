import styles from "@/components/HomeContent/HomeContent.module.css";
import Loading from "../Loading";
import axios from "axios";
// useEffect -> efeito colateral; assim que o componente é renderizado, ele é disparado, nesse caso o get pra mostrar os jogos
import { useState, useEffect } from "react";

const HomeContent = () => {
  // criando um estado para games
  const [games, setGames] = useState([]);
  // estado para o loading
  const [loading, setLoading] = useState(true);
  // efeito colateral
  useEffect(() => {
    const fetchGames = async () => {
      try {
        // faz a requisição para o backend; como se fosse no insomnia
        const response = await axios.get("http://localhost:4000/games");
        // console.log(response);
        // pegando a lista de ga,es e colocando no estado
        setGames(response.data.games);
      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    };
    // invocando a função para que o efeito colateral funcione
    fetchGames();
  }, []); // dependência do useEffect, info que ele vai usar pra ser executado novamente

  // função para deletar
  const deleteGame = async (gameId) => {
    try {
      const response = await axios.delete(
        `http://localhost:4000/games/${gameId}`
      );
      if (response.status === 204) {
        alert("Jogo excluído com sucesso!");
        setGames(games.filter(game => game._id !== gameId))
      }
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <>
      <div className={styles.homeContent}>
        {/* CARD LISTA DE JOGOS */}
        <div className={styles.listGamesCard}>
          {/* TITLE */}
          <div className={styles.title}>
            <h2>Lista de jogos</h2>
          </div>
          {/* GIF de carregamento*/}
          <Loading loading={loading} />
          <div className={styles.games} id={styles.games}>
            {/* Lista de jogos irá aqui */}
            {games.map((game) => (
              <ul key={game._id} className={styles.listGames}>
                <div className={styles.gameImg}>
                  <img src="images/game_cd_cover.png" alt="Jogo em estoque" />
                </div>
                <div className={styles.gameInfo}>
                  <h3>{game.title}</h3>
                  <li>Plataforma: {game.descriptions.plataform}</li>
                  <li>Gênero: {game.descriptions.genre}</li>
                  <li>Classificação: {game.descriptions.rating}</li>
                  <li>Ano: {game.year}</li>
                  <li>
                    Preço:{" "}
                    {game.price.toLocaleString("pt-br", {
                      style: "currency",
                      currency: "BRL",
                    })}
                  </li>
                  {/* Botão para excluir */}
                  <button
                    className={styles.btnDel}
                    onClick={() => {
                      const confirmed = window.confirm(
                        "Deseja mesmo exluir o jogo?"
                      );
                      if (confirmed) {
                        deleteGame(game._id);
                      }
                    }}
                  >
                    Deletar
                  </button>
                </div>
              </ul>
            ))}
          </div>
        </div>
      </div>
    </>
  );
};

export default HomeContent;
