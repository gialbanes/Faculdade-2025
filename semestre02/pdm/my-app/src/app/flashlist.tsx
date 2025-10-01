import { FlashList } from '@shopify/flash-list';
import { useEffect, useState } from "react";
import { FlatList, Text, View } from "react-native";

const API_URL = 'https://jsonplaceholder.typicode.com/photos?_limit=1000'

export default function FlatListFetch (){
    const [data, setData] =  useState();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // função que vai receber a API 
        fetch(API_URL)
        .then((response) => response.json())
        // vai declarar explicitamente que é um json e armazenar na variável data
        .then((json) => setData(json))
        // tratamento de erro 
        .catch((error) => console.error(error))
        .finally(() => setLoading(false))
    })

    return (
        // não é comum eu decorar esse componente, mas devo saber o que é e pra que serve 
        // passo um objeto e ele faz a interação em cada um 
        <FlashList
            data={data}
            // para ele se localizar com os id, é essencial
            keyExtractor={(item) => item.id.toString()}
            onViewableItemsChanged={({viewableItems, changed}) => {
                console.log("Itens visíveis:", viewableItems.map(item => item.key));
                console.warn("Itens alterados:", changed.map(item => item.key));
            }}
            renderItem={({item}) => (
                <View style={{padding:16}}>
                    <Text numberOfLines={2}>
                        {item.id}: {item.title}
                    </Text>
                </View>
            )}
        />
    )
}