  import styles from "@/components/LoginContent/LoginContent.module.css";
  import { useRouter } from "next/router";
  import { useState } from "react";
  import { login } from "@/services/auth"; // importando a função de login do serviço de autenticação

  const LoginContent = () => {
    const router = useRouter();
    // criando os estados para os dados
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
""
    const handleLogin = async (e) => {
      // impede o comportamento padrão do formulário
      e.preventDefault();
      // aqui irá a validção, autenticação etc
      const result = await login(email, password);
      if (result.success) {
        alert("Login realizado com sucesso!");
        // redireciona para a página inicial
        router.push("/home");
      } else {
        alert("Falha ao fazer o login. tente novamente!");
      }
    };

    return (
      <div className={styles.loginContent}>
        {/* LOGO */}
        <div className={styles.logo}>
          <img
            src="/images/thegames_logo.png"
            className={styles.logoImg}
            alt="The Games"
          />
        </div>
        {/* LOGIN CARD */}
        <div className={styles.loginCard}>
          {/* LOGIN CARD HEADER */}
          <div className={styles.loginCardHeader}>
            <h3>Faça seu login:</h3>
          </div>
          {/* LOGIN CARD BODY */}
          <div className={styles.loginCardBody}>
            <form className="formPrimary" onSubmit={handleLogin}>
              <input
                type="email"
                name="email"
                id="email"
                placeholder="Digite seu e-mail"
                className={`${styles.input} ${"inputPrimary"}`}
                // para capturar oq o usuário digitar no input
                // chamo um evento para alterar o estado do email
                onChange={(e) => setEmail(e.target.value)}
                value={email} // para que o valor do input seja o mesmo que o estado
              />
              <input
                type="password"
                name="password"
                id="password"
                placeholder="Digite sua senha"
                className={`${styles.input} ${"inputPrimary"}`}
                onChange={(e) => setPassword(e.target.value)}
                value={password} // para que o valor do input seja o mesmo que o estado
              />
              <button type="submit" className={`${styles.input} ${"btnPrimary"}`}>
                Entrar
              </button>
            </form>
          </div>
        </div>
      </div>
    );
  };

  export default LoginContent;
