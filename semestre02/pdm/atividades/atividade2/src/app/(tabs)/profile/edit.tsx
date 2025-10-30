import Button from "@/components/Button";
import { ProfileStorage } from "@/services/profileStorage";
import { Profile } from "@/types/profile";
import { router, useFocusEffect } from "expo-router";
import { useCallback, useState } from "react";
import {
    StyleSheet,
    Text,
    TextInput,
    View
} from "react-native";

export default function EditProfileModal() {
  const [name, setName] = useState("");
  const [lastName, setLastName] = useState("");
  const [age, setAge] = useState("");
  const [institution, setInstitution] = useState("");
  const [course, setCourse] = useState("");

  useFocusEffect(
    useCallback(() => {
      async function loadProfile() {
        const savedProfile = await ProfileStorage.load();

        if (savedProfile) {
          setName(savedProfile.name);
          setLastName(savedProfile.lastName || "");
          setAge(savedProfile.age?.toString() || "");
          setInstitution(savedProfile.institution || "");
          setCourse(savedProfile.course || "");
        }
      }

      loadProfile();
    }, [])
  );


  const handleSave = async () => {
    const updatedProfile: Profile = {
      name: name.trim(),
      lastName: lastName.trim() || undefined,
      age: age ? parseInt(age) : undefined,
      institution: institution.trim() || undefined,
      course: course.trim() || undefined,
    };

    await ProfileStorage.save(updatedProfile);
    handleCancel();
  };

  const handleCancel = () => {
    router.back();
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Editar Perfil</Text>

      {/* Informações do Perfil */}
      <View style={styles.profileInfo}>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Nome:</Text>
          <TextInput
            style={styles.textInput}
            value={name}
            onChangeText={setName}
            placeholder="Digite seu nome"
            placeholderTextColor="#999999"
          />
        </View>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Sobrenome:</Text>
          <TextInput
            style={styles.textInput}
            value={lastName}
            onChangeText={setLastName}
            placeholder="Digite seu sobrenome"
            placeholderTextColor="#999999"
          />
        </View>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Idade:</Text>
          <TextInput
            style={styles.textInput}
            value={age}
            onChangeText={setAge}
            placeholder="Digite sua idade"
            placeholderTextColor="#999999"
            keyboardType="numeric"
          />
        </View>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Instituição:</Text>
          <TextInput
            style={styles.textInput}
            value={institution}
            onChangeText={setInstitution}
            placeholder="Digite sua instituição"
            placeholderTextColor="#999999"
          />
        </View>

        <View style={styles.infoItem}>
          <Text style={styles.infoLabel}>Curso:</Text>
          <TextInput
            style={styles.textInput}
            value={course}
            onChangeText={setCourse}
            placeholder="Digite seu curso"
            placeholderTextColor="#999999"
          />
        </View>
      </View>

      <View style={styles.footer}>
        <Button title="SALVAR" onPress={handleSave} />
        <Button title="Cancelar" variant="outline" onPress={handleCancel} />
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
    marginBottom: 20,
  },
  infoLabel: {
    fontSize: 16,
    fontWeight: "600",
    color: "#0077b5",
    marginBottom: 8,
    marginLeft: 4,
  },
  textInput: {
    fontSize: 16,
    paddingVertical: 16,
    paddingHorizontal: 20,
    backgroundColor: "#ffffff",
    borderRadius: 12,
    borderWidth: 2,
    borderColor: "#e1f5fe",
    color: "#333333",
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 1,
    },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  footer: {
    paddingHorizontal: 20,
    paddingBottom: 40,
    paddingTop: 20,
    gap: 16,
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
