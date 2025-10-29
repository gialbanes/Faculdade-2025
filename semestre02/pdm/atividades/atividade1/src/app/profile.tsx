import Button from "@/components/Button";
import { Alert, Image, Linking, StyleSheet, Text, TouchableOpacity, View } from "react-native";

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

    return(
        <>
        <View style={styles.container}>
                <Image
                    source={{ uri: "https://github.com/gialbanes.png"}}
                    style={styles.profileImage}
                />
            <Text style={styles.title}>Giovana Albanês</Text>

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
    backgroundColor: "#ffffff",
    padding: 20,
    gap: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 24,
  },
  footer: {
    width: "100%",
    gap: 12,
    paddingBottom: 40,
  },
  profileImage: {
    width: 120,
    height: 120,
    borderRadius: 60,
  },
  profileInfo: {
    width: "100%",
    marginBottom: 40,
  },
  infoItem: {
    marginBottom: 20,
    paddingHorizontal: 10,
  },
  infoLabel: {
    fontSize: 14,
    fontWeight: "600",
    color: "#666666",
    marginBottom: 5,
  },
  infoValue: {
    fontSize: 18,
    fontWeight: "500",
    color: "#333333",
    paddingVertical: 10,
    paddingHorizontal: 15,
    backgroundColor: "#f8f8f8",
    borderRadius: 8,
    borderWidth: 1,
    borderColor: "#e0e0e0",
  },
});
