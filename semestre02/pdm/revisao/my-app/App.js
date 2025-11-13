import { Button, FlatList, Text, View, Image } from 'react-native';
import  { useEffect, useState } from 'react';

const LOCAL_DATA = [
  {id: "1", title: "Item 1", description: "Descrição do Item 1"},
  {id: "2", title: "Item 2", description: "Descrição do Item 2"},
  {id: "3", title: "Item 3", description: "Descrição do Item 3"},
  {id: "4", title: "Item 4", description: "Descrição do Item 4"},
  {id: "5", title: "Item 5", description: "Descrição do Item 5"},
  {id: "6", title: "Item 6", description: "Descrição do Item 6"},
  {id: "7", title: "Item 7", description: "Descrição do Item 7"},
  {id: "8", title: "Item 8", description: "Descrição do Item 8"},
  {id: "9", title: "Item 9", description: "Descrição do Item 9"},
]

const API_URL = "https://jsonplaceholder.typicode.com/photos?_limit=1000";

export default function App() {
  // não vai cair useState na prova
  const [data, setData] = useState([]);

  // função para buscar dados da API ao montar o componente
  useEffect(() => {
    fetch(API_URL)
    .then((response) => response.json())
    .then((json) => setData(json))
    .catch((error) => console.error(error));
  }, []); // array vazio para rodar apenas uma vez nese caso, mas se tivesse callback eu passaria a ouutras variáveis aqui 

  // como vai renderizar algo, deve-se usar ()
  const render = ({item}) => (
    // desestruturar os itens 
    <View>
      <Image style={{width: 100, height: 100}} source={{uri: "https://images.unsplash.com/photo-1541643600914-78b084683601?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=2008"}}
      />
      <View>
        <Text>{item.title}</Text>
        <Text>{item.url}</Text>
      </View>
      <Button title="Adicionar item" color="#1d1d1d"/>
    </View>

  )

  // estrutura base para iniciar FlatList: data, renderItem e keyExtractor
  // como montar uma flatlist e as propriedades que ela precisa
  return (
    <FlatList
    // dados da lista
    // pode vir do banco ou API externa 
    data={data}
    // renderiza cada item da lista
    renderItem={render}
    // chave única para cada item da lista para não se perder entre os itens renderizados e excluídos 
    keyExtractor={(item) => item.id}
    />
  );
}

