// Importando o hook useState
import { useState } from "react";

const TrafficLight = () => {
    // Criando o estado para manipular as cores
    // [color = consulta o valor / setColor = altera o valor]
    const [color, setColor] = useState("gray")

  return (
    <>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <h3>Semáforo:</h3>
        <br />
        <div
          style={{
            backgroundColor: color == "red" ? color : "gray",
            borderRadius: "50%",
            width: "100px",
            height: "100px",
          }}
        ></div>
        <div
          style={{
            backgroundColor: color == "yellow" ? color : "gray",
            borderRadius: "50%",
            width: "100px",
            height: "100px",
          }}
        ></div>
        <div
          style={{
            backgroundColor: color == "green" ? color : "gray",
            borderRadius: "50%",
            width: "100px",
            height: "100px",
          }}
        ></div>
        <br />
        {/* Botões */}
        <div>
          <button onClick={() => setColor("red")}>Pare!</button>&nbsp;
          <button onClick={() => setColor("yellow")}>Atenção!</button>&nbsp;
          <button onClick={() => setColor("green")}>Siga!</button>
        </div>
      </div>
    </>
  );
};
export default TrafficLight;
