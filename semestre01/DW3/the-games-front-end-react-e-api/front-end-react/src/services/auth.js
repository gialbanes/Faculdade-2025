// a pasta services vai conter os serviços de login (a pasta pode ter outros nomes)
import axios from "axios";

// criando um objeto para ser o cabeçalho da requisição
export const axiosConfig = {
  headers: {
    // eu manipulo o localStorage do navegador, não o do servidor
    // se for no navegador, o localStorage é um objeto que armazena dados, ou seja, não é undefined
    authorization: `Bearer ${
      typeof window !== "undefined" ? localStorage.getItem("token") : ""
    }`, // se tiver, exibe o token, se não tiver, exibe uma string vazia
  },
};

// função de login
// recebe email e passowrd
export const login = async (email, password) => {
  try {
    // enviando uma req post para realizar o login - feita por meio do axios
    // a varíavel vai ser um objeto com vários atributos da resposta da API
    const response = await axios.post("http://localhost:4000/auth", {
      email, // o email e a senha são passados como atributos do objeto, ou seja, o corpo da requisição - assimilando com o insomnia
      password,
    });
    const token = response.data.token; // o token é o objeto retornado na resposta da API
    // console.log(token);
    // gravando o token no localStorage do navegador
    localStorage.setItem("token", token); // campo, valor

    // atualizando o token que está no navegador ao fazer o login
    axiosConfig.headers.authorization = `Bearer ${token}`;
    return { success: true }; // se o login for bem sucedido, retorna um objeto com a propriedade success como true
  } catch (error) {
    console.log(error);
    return { success: false, message: error.message }; // se o login falhar, retorna um objeto com a propriedade success como false
  }
};

// função de logout
export const logout = (router) => {
  localStorage.removeItem("token"); // remove o token do localStorage do navegador
  axiosConfig.headers.authorization = ""; // remove o token do cabeçalho da requisição
  // não posos importar o router fora de um componente, então eu importo no componente Menu e chamo aqui 
  router.push("/"); // redireciona para a página inicial
};
