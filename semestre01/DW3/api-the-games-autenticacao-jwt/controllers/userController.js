import userService from "../services/userService.js";
import jwt from "jsonwebtoken";
//JWTSecret
const JWTSecret = "apigamessecret";

// cadastrando um usuário
const createUser = async (req, res) => {
  try {
    const { name, email, password } = req.body;
    await userService.Create(name, email, password);
    res.sendStatus(201); // Created
  } catch (error) {
    console.log(error);
    res.sendStatus(500); // Erro interno do servidor
  }
};

// Autenticando um usuário
const loginUser = async (req, res) => {
  try {
    const { email, password } = req.body;
    // se o email não está vazio
    if (email != undefined) {
      // busca o usuário no banco
      const user = await userService.getOne(email);
      // usuário encontrado (se está cadastrado)
      if (user != undefined) {
        // senha correta
        if (user.password == password) {
          // gerando o token
          // infos passadas ao gerar o token
          // segredo: uma String para incrementar a segurança; está definida como variável no início do código; geralmente ele vai na variável de ambiente;
          // arrow function para gravar o erro; se deu, ele vai gravar na variável token
          jwt.sign(
            { id: user._id, email: user.email },
            JWTSecret,
            { expiresIn: "48h" },
            (error, token) => {
              if (error) {
                res.status(400).json({ error: "Erro ao gerar o token." }); // bad request
              } else {
                res.status(200).json({ token: token });
              }
            }
          );
          //Senha incorreta
        } else {
          res.status(401).json({ error: "Credenciais inválidas." }); //Unauthorized
        }
        // usuário não encontrado
      } else {
        res.status(404).json({ error: "Usuário não encontrado." }); // Not found
      }
    } else {
      res.status(400).json({ error: "O email enviado é inválido." }); // bad request
    }
  } catch (error) {
    console.log(error);
    sendStatus(500); //Erro interno do servidor
  }
};

export default { createUser, loginUser };
