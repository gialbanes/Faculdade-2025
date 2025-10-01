import { FlatList, View } from "react-native";
import Card from "../components/Card";

const LOCAL_DATA =  [
    {id: 1, title: 'Item 1', body: 'Descrição do item 1'},
    {id: 2, title: 'Item 2', body: 'Descrição do item 2'},
    {id: 3, title: 'Item 3', body: 'Descrição do item 3'},
    {id: 4, title: 'Item 4', body: 'Descrição do item 4'},
    {id: 5, title: 'Item 5', body: 'Descrição do item 5'},
    {id: 6, title: 'Item 6', body: 'Descrição do item 6'},
    {id: 7, title: 'Item 1', body: 'Descrição do item 1'},
    {id: 8, title: 'Item 2', body: 'Descrição do item 2'},
    {id: 9, title: 'Item 3', body: 'Descrição do item 3'},
    {id: 10, title: 'Item 4', body: 'Descrição do item 4'},
    {id: 11, title: 'Item 5', body: 'Descrição do item 5'},
    {id: 12, title: 'Item 6', body: 'Descrição do item 6'},
]
export default function FlatListExample (){
    return (
        // não é comum eu decorar esse componente, mas devo saber o que é e pra que serve 
        // passo um objeto e ele faz a interação em cada um 
        <FlatList
            data = {LOCAL_DATA}
            // para ele se localizar com os id, é essencial
            keyExtractor={(item) => item.id.toString()}
            onViewableItemsChanged={({viewableItems, changed}) => {
                console.log("Itens visíveis:", viewableItems.map(item => item.key));
                console.warn("Itens alterados:", changed.map(item => item.key));
            }}
            renderItem={({item}) => (
                <View style={{padding:16}}>
                    <Card title={item.title} body={item.body} href={" "}></Card>
                </View>
            )}
        />
    )
}