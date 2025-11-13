import { FlatList, Text, View, Image, StyleSheet } from 'react-native';
import { useEffect, useState } from 'react';

const API_URL = "https://fakestoreapi.com/products"

export default function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => console.error(error));
  }, []);

  const render = ({item}) => (
    <View style={styles.itemContainer}>
      <Image style={styles.image} source={{uri: item.image}} />
      <Text style={styles.titulo} numberOfLines={2}>{item.title}</Text>
      <Text style={styles.preco}>Preço: ${item.price}</Text>
      <Text style={styles.descricao} numberOfLines={2}>{item.description}</Text>
      <Text style={styles.categoria}>Categoria: {item.category}</Text>
      {item.rating && (
        <Text style={styles.rating}>Rating: {item.rating.rate} ({item.rating.count})</Text>
      )}
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Itens da loja</Text>
      <FlatList
        data={data}
        renderItem={render}
        keyExtractor={item => item.id}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: 50,
  },
  header: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
    color: '#333',
  },
  itemContainer: {
    padding: 15,
    margin: 10,
    backgroundColor: '#f0f0f0',
    borderRadius: 5,
  },
  image: {
    width: 150, 
    height: 150,
    alignSelf: 'center',
    marginBottom: 10,
  },
  titulo: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  preco: {
    fontSize: 14,
    color: 'green',
    marginBottom: 5,
  },
  descricao: {
    fontSize: 12,
    color: '#666',
    marginBottom: 5,
  },
  categoria: {
    fontSize: 13,
    color: 'blue',
    marginBottom: 5,
  },
  rating: {
    fontSize: 12,
    color: '#888',
  },
});

