import { Stack } from "expo-router";
import { StatusBar } from "expo-status-bar";

export default function RootLayout(){
    return (
        <>
        <StatusBar style='auto' />
        <Stack initialRouteName="(tabs)/home">
            <Stack.Screen name="(tabs)/home" options={{ headerShown: false }} />
        </Stack>
        </>
    )
}
