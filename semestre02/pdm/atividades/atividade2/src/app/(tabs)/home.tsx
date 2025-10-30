import { useRouter } from 'expo-router';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export default function HomePage() {
    const router = useRouter();

    const callProfile = () => {
        router.push('/profile/profile');
    };

    return(
        <View style={styles.container}>
            <View style={styles.header}>
                <View style={styles.logoContainer}>
                    <Text style={styles.logo}>in</Text>
                </View>
                <Text style={styles.title}>Bem-vindo(a) ao LinkedIn!</Text>
            </View>
            
            <View style={styles.content}>
                <View style={styles.card}>
                    <Text style={styles.cardTitle}>Comece sua jornada</Text>
                    <Text style={styles.cardDescription}>
                        Criamos um perfil padrão pra você!
                    </Text>
                    <TouchableOpacity style={styles.button} onPress={callProfile}>
                        <Text style={styles.buttonText}>Visualizar perfil</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f8f9fa",
  },
  header: {
    padding: 24,
    paddingTop: 60,
    backgroundColor: "linear-gradient(135deg, #0077b5 0%, #00a0dc 100%)",
    borderBottomLeftRadius: 24,
    borderBottomRightRadius: 24,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 8,
  },
  logoContainer: {
    width: 50,
    height: 50,
    backgroundColor: "#ffffff",
    borderRadius: 8,
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 16,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 4,
  },
  logo: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#0077b5",
  },
  title: {
    fontSize: 26,
    fontWeight: "bold",
    color: "#0077b5",
    marginBottom: 8,
    lineHeight: 32,
  },
  content: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  card: {
    backgroundColor: "#ffffff",
    borderRadius: 16,
    padding: 24,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.08,
    shadowRadius: 12,
    elevation: 4,
    borderLeftWidth: 4,
    borderLeftColor: "#0077b5",
    width: "100%",
    maxWidth: 350,
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#1a1a1a",
    marginBottom: 12,
    lineHeight: 26,
  },
  cardDescription: {
    fontSize: 16,
    color: "#666666",
    lineHeight: 24,
    marginBottom: 20,
  },
  button: {
    backgroundColor: "#0077b5",
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
    alignItems: "center",
    shadowColor: "#0077b5",
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 6,
  },
  buttonText: {
    color: "#ffffff",
    fontSize: 16,
    fontWeight: "600",
  },
});

