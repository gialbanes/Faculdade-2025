import jwt from "jsonwebtoken";
import userController from "../controllers/userController.js";

// função para checagem da autenticação
// chamo o next para liberar o acesso se tiver o token
const Authorization = (req, res, next) => {
  // coletar o token do cabeçalho da requisição
  const authToken = req.headers["authorization"];
  if (authToken != undefined) {
    // dividindo o token
    // tenho que usar .split() pra cortar o Bearer, logo, o meu token está na posição 1 do meu array
    const bearer = authToken.split(" ");
    const token = bearer[1];
    // validando o token
    jwt.verify(token, userController.JWTSecret, (error, data) => {
      if (error) {
        res.status(401).json({ error: "Token inválido. Não autorizado." }); // código de não autorizado
      } else {
        // token válido
        // grava o token como um objeto para a requisição
        req.token = token;
        req.loggedUser = {
          id: data.id,
          email: data.email,
        };
        next();
      }
    });
  } else {
    res.status(401).json({ error: "Token inválido. Não possuo token." }); // código de não autorizado
  }
};

export default { Authorization };
