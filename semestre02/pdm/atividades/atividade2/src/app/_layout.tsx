import { Stack } from "expo-router";
import { StatusBar } from "expo-status-bar";

export default function RootLayout(){
    return (
        <>
        <StatusBar style='auto' />
        <Stack initialRouteName="(tabs)/home">
            <Stack.Screen name="(tabs)/home" options={{ headerShown: false }} />
            <Stack.Screen 
                name="(tabs)/profile/profile" 
                options={{ 
                    headerShown: true,
                    title: "Perfil",
                    headerBackTitle: "Voltar"
                }} 
            />
            <Stack.Screen 
                name="(tabs)/profile/edit" 
                options={{ 
                    headerShown: true,
                    title: "Editar Perfil",
                    headerBackTitle: "Perfil"
                }} 
            />
        </Stack>
        </>
    )
}
