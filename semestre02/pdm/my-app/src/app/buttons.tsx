import { Button, View, StyleSheet, TouchableOpacity, Text, Pressable } from "react-native";

export default function Buttons(){
    return(
        <View style={styles.container}>
            <Button title="Botão padrão"/>

            {/* Nesse eu não posso mudar muita coisa, apenas opacidade e estilo */}
            <TouchableOpacity activeOpacity={0.8} style={styles.button}>
                <Text style={styles.text}>TouchableOpacity</Text>
            </TouchableOpacity>

            {/* Pressable - maior controle e funcionalidades */}
            {/* Esse é mais atualizado e configurado, consigo controlar cada evento */}
            <Pressable style={styles.button}
            // cada um desses é um evento
            onPress={() => console.log("Clicou no botão")}
            onLongPress={() => console.warn("Segurou no botão")}
            onPressOut={() => console.log("Largou do botão")}
            delayLongPress={2000}
            >
                <Text style={styles.text}>Pressable</Text>
            </Pressable>

            {/* Voltar */}
            {/* <TouchableOpacity onPress={() => router.back()}>
                <Text style={styles.backLink}>Voltar</Text>
            </TouchableOpacity> */}
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        padding: 32,
        gap: 16,
        backgroundColor: "#f0f0f0"
    },
    button: {
        backgroundColor: "#1d1d1d",
        paddingVertical: 16, 
        alignItems: "center",
        borderRadius: 8
    },
    text: {
        color: "#dfdfdf",
        fontSize: 16,
        fontWeight: 'bold'
    },
    backLink: {
        textAlign: 'center',
        color: '#333',
        marginTop: 16,
    }

})