import styles from "@/components/EditContent/EditContent.module.css";
import { useState, useEffect } from "react";
import axios from "axios";

const EditContent = ({ onClose, game }) => {
  // criando os estados para as informações do jogo
  const [id, setId] = useState("");
  const [title, setTitle] = useState("");
  const [platform, setPlatform] = useState("");
  const [genre, setGenre] = useState("");
  const [rating, setRating] = useState("");
  const [year, setYear] = useState("");
  const [price, setPrice] = useState("");

  // o useEffect é usado quando o componente for chamado, é o efeito colateral -> quando eu pegar o jogo as infos dele devem ser exibidas
  // sempre que eu quero infos de um componente e jogar p outro uso props
  useEffect(() => {
    if (game) {
      setId(game._id);
      setTitle(game.title);
      setPlatform(game.descriptions.platform);
      setGenre(game.descriptions.genre);
      setRating(game.descriptions.rating);
      setYear(game.year);
      setPrice(game.price);
    }
  }, [game]); // toda vez que o game mudar, o useEffect vai ser chamado -> é uma dependência que faz o useEffect ser executado novamente

  // função para tratar submissão do formulário
  const handleSubmit = async (event) => {
    event.preventDefault();

    const updatedGame = {
      title,
      year,
      price,
      descriptions: {
        platform,
        genre,
        rating,
      },
    };
    // enviando para API
    try {
      const response = await axios.put(`htppd://localhost:4000/games${id}`, updatedGame);
      if (response.status === 200) {
        alert("O jogo foi alterado com sucesso!");
        onClose();
      }
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <>
      {/* CARD EDIÇÃO */}
      <div className={styles.editModal} id={styles.editModal}>
        <div className={styles.editContent}>
          <span className={styles.modalClose} onClick={onClose}>
            &times;
          </span>
          {/* TITLE */}
          <div className="title">
            <h2>Editar jogo</h2>
          </div>
          <form id="editForm">
            <input type="hidden" name="id" value={id} />
            <input
              type="text"
              name="title"
              placeholder="Insira o novo título"
              className="inputPrimary"
              required
              value={title}
            />
            <input
              type="text"
              name="platform"
              placeholder="Insira a nova plataforma do jogo"
              className="inputPrimary"
              required
              value={platform}
            />
            <input
              type="text"
              name="genre"
              placeholder="Insira o gênero do jogo"
              className="inputPrimary"
              required
              value={genre}
            />
            <input
              type="text"
              name="rating"
              placeholder="Insira a classificação do jogo"
              className="inputPrimary"
              required
              value={rating}
            />
            <input
              type="number"
              name="year"
              placeholder="Insira o novo ano"
              className="inputPrimary"
              required
              value={year}
            />
            <input
              type="text"
              name="price"
              placeholder="Insira o novo preço"
              className="inputPrimary"
              required
              value={price}
            />
            <input type="submit" value="Alterar" className="btnPrimary" />
          </form>
        </div>
      </div>
    </>
  );
};

export default EditContent;
