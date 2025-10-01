import { TextInput, View, StyleSheet } from "react-native";

export default function Inputs(){
    return (
        <View style={styles.container}>
            <TextInput style={styles.input} placeholder="Digite seu username"></TextInput>
            <TextInput style={styles.input} placeholder="Digite sua senha" secureTextEntry={true}></TextInput>
            <TextInput style={styles.input} placeholder="Digite seu telefone" keyboardType="phone-pad"></TextInput>
            <TextInput style={styles.input} placeholder="Digite seu telefone" keyboardType="number-pad"></TextInput>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        padding: 16,
        gap: 16
    },
    input: {
        borderWidth: 1, 
        borderColor: '#ccc',
        borderRadius: 4, 
        padding: 12,
        marginVertical: 8
    }
})