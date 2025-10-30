import Button from "@/components/Button";
import { ProfileStorage } from "@/services/profileStorage";
import { Profile } from "@/types/profile";
import { router, useFocusEffect } from "expo-router";
import { useCallback, useState } from "react";
import { StyleSheet, Text, View } from "react-native";

export default function ProfileScreen() {
  const [profile, setProfile] = useState<Profile>({
    name: "",
    lastName: "",
    age: 0,
    institution: "",
    course: ""
  });

  useFocusEffect(
    useCallback(() => {
      async function loadProfile() {
        const savedProfile = await ProfileStorage.load();

        if (savedProfile) {
          setProfile(savedProfile);
        }
      }

      loadProfile();
    }, [])
  );

  const handleEditProfile = () => {
    router.push("/profile/edit");
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Meu Perfil</Text>

      <View style={styles.profileInfo}>
        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Nome:</Text>
          <Text style={styles.infoValue}>{profile.name}</Text>
        </View>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Sobrenome:</Text>
          <Text style={styles.infoValue}>{profile.lastName || "Não informado"}</Text>
        </View>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Idade:</Text>
          <Text style={styles.infoValue}>{profile.age ? `${profile.age} anos` : "Não informado"}</Text>
        </View>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Instituição:</Text>
          <Text style={styles.infoValue}>{profile.institution || "Não informado"}</Text>
        </View>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Curso:</Text>
          <Text style={styles.infoValue}>{profile.course || "Não informado"}</Text>
        </View>
      </View>

      <View style={styles.footer}>
        <Button title="EDITAR PERFIL" onPress={handleEditProfile} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f8f9fa",
    paddingTop: 60,
  },
  title: {
    fontSize: 28,
    fontWeight: "bold",
    color: "#0077b5",
    textAlign: "center",
    marginBottom: 32,
    paddingHorizontal: 20,
  },
  profileInfo: {
    flex: 1,
    paddingHorizontal: 20,
    paddingBottom: 20,
  },
  infoItem: {
    marginBottom: 16,
    backgroundColor: "#ffffff",
    borderRadius: 12,
    padding: 16,
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 1,
    },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  infoLabel: {
    fontSize: 14,
    fontWeight: "600",
    color: "#0077b5",
    marginBottom: 8,
    textTransform: "uppercase",
    letterSpacing: 0.5,
  },
  infoValue: {
    fontSize: 18,
    fontWeight: "500",
    color: "#333333",
    lineHeight: 24,
  },
  footer: {
    paddingHorizontal: 20,
    paddingBottom: 40,
    paddingTop: 20,
    backgroundColor: "#ffffff",
    borderTopLeftRadius: 24,
    borderTopRightRadius: 24,
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: -2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 8,
  },
});
