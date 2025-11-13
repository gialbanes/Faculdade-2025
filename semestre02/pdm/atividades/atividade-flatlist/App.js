import { Button, FlatList, Text, View, Image, StyleSheet } from 'react-native';


const PIZZARIA_DATA = [
  {id: '1', nome: "Marguerita", descricao: "Molho de tomate, mussarela, manjericão", valor: 25.00},
  {id: '2', nome: "Pepperoni", descricao: "Molho de tomate, mussarela, pepperoni", valor: 30.00},
  {id: '3', nome: "Quatro Queijos", descricao: "Molho de tomate, mussarela, gorgonzola, parmesão, catupiry", valor: 35.00},
  {id: '4', nome: "Portuguesa", descricao: "Molho de tomate, mussarela, presunto, ovos, cebola, azeitonas", valor: 28.00},
  {id: '5', nome: "Frango com Catupiry", descricao: "Molho de tomate, mussarela, frango desfiado, catupiry", valor: 32.00},
  {id: '6', nome: "Calabresa", descricao: "Molho de tomate, mussarela, calabresa, cebola", valor: 27.00},
  {id: '7', nome: "Vegetariana", descricao: "Molho de tomate, mussarela, legumes variados", valor: 26.00},
  {id: '8', nome: "Baiana", descricao: "Molho de tomate, mussarela, calabresa, ovo, pimenta", valor: 29.00},
  {id: '9', nome: "Napolitana", descricao: "Molho de tomate, mussarela, tomate fatiado, alho, orégano", valor: 24.00},
  {id: '10', nome: "Chocolate", descricao: "Chocolate derretido, morangos", valor: 22.00}
]

export default function App() {
  const render = ({item}) => (
    <View style={styles.itemContainer}>
      <Image 
        style={styles.pizzaImage} 
        source={{uri: "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGl6emF8ZW58MHx8MHx8fDA%3D"}}
      />
      <View style={styles.infoContainer}>
        <Text style={styles.pizzaName}>{item.nome}</Text>
        <Text style={styles.pizzaDescription}>{item.descricao}</Text>
        <Text style={styles.pizzaPrice}>R$ {item.valor.toFixed(2)}</Text>
      </View>
      <View style={styles.buttonContainer}>
        <Button title="Adicionar" color={"#e74c3c"}/>
      </View>
    </View>
  ) 

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Pizzaria Saborear</Text>
      <Text style={styles.header}>Cananéia</Text>
      <FlatList
        data={PIZZARIA_DATA}
        renderItem={render}
        keyExtractor={item => item.id}
        showsVerticalScrollIndicator={false}
        contentContainerStyle={styles.listContainer}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
    paddingTop: 50,
  },
  header: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
    color: '#2c3e50',
    textShadowColor: 'rgba(0, 0, 0, 0.1)',
    textShadowOffset: {width: 1, height: 1},
    textShadowRadius: 2,
  },
  listContainer: {
    paddingHorizontal: 15,
    paddingBottom: 20,
  },
  itemContainer: {
    backgroundColor: '#ffffff',
    marginBottom: 15,
    borderRadius: 12,
    padding: 15,
    flexDirection: 'row',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 3.84,
    elevation: 5,
    borderLeftWidth: 4,
    borderLeftColor: '#e74c3c',
  },
  pizzaImage: {
    width: 80,
    height: 80,
    borderRadius: 40,
    marginRight: 15,
    borderWidth: 2,
    borderColor: '#ecf0f1',
  },
  infoContainer: {
    flex: 1,
    justifyContent: 'center',
  },
  pizzaName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#2c3e50',
    marginBottom: 5,
  },
  pizzaDescription: {
    fontSize: 14,
    color: '#7f8c8d',
    marginBottom: 8,
    lineHeight: 18,
  },
  pizzaPrice: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#27ae60',
  },
  buttonContainer: {
    marginLeft: 10,
  },
});

