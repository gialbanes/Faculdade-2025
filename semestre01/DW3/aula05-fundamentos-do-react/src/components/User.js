const User = () => {
  // Criando variáveis
  const name = "Giovana";
  return (
    // return + () significa que vou retornar jsx
    <>
      <div>
        {/* Expressão JSX - toda vez que uso chaves - posso incluir variáveis, cálculos */}
        <p>Bem-indo, {nome}</p>
      </div>
    </>
  );
};
export default User;
