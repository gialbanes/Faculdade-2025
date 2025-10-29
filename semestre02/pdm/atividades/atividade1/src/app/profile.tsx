import Button from "@/components/Button";
import { Alert, Image, Linking, Pressable, StyleSheet, Text, TouchableOpacity, View } from "react-native";

export default function Profile() {
    const handleOpenGitHub = async () => {
        const url = "https://github.com/gialbanes";
        try {
            const supported = await Linking.canOpenURL(url);
            if (supported) {
                await Linking.openURL(url);
            }
        } catch (error) {
            Alert.alert("Erro", "Ocorreu um erro ao tentar abrir o GitHub");
        }
    };

    const handlePressableAction = () => {
        Alert.alert("Pressable", "Você clicou na imagem usando Pressable!");
    };

    const handleTouchableAction = () => {
        Alert.alert("TouchableOpacity", "Você clicou no nome usando TouchableOpacity!");
    };

    return(
        <>
        <View style={styles.container}>
            <Pressable 
                style={({ pressed }) => [
                    styles.profileImageContainer,
                    { opacity: pressed ? 0.8 : 1 }
                ]}
                onPress={handlePressableAction}
            >
                <Image
                    source={{ uri: "https://github.com/gialbanes.png"}}
                    style={styles.profileImage}
                />
            </Pressable>
            
            <TouchableOpacity 
                activeOpacity={0.7}
                onPress={handleTouchableAction}
            >
                <Text style={styles.title}>Giovana Albanês</Text>
            </TouchableOpacity>

            <View style={styles.footer}>
                <Button title="Ver perfil no GitHub" onPress={handleOpenGitHub}/>
            </View>
        </View>
        </>
    )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f5f7fa",
    padding: 24,
    gap: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: "700",
    color: "#2c3e50",
    marginBottom: 8,
    textAlign: "center",
    letterSpacing: 0.5,
  },
  footer: {
    width: "100%",
    marginTop: 32,
    paddingHorizontal: 16,
  },
  profileImageContainer: {
    borderRadius: 70,
    borderWidth: 4,
    borderColor: "#007bff",
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 4,
    },
    shadowOpacity: 0.3,
    shadowRadius: 6,
    elevation: 8,
  },
  profileImage: {
    width: 140,
    height: 140,
    borderRadius: 70,
  },
});
