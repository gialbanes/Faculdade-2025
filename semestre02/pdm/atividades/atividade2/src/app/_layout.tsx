import { useFonts } from 'expo-font';
import { Stack } from "expo-router";
import { StatusBar } from "expo-status-bar";

export default function RootLayout(){
    const [loaded] = useFonts({
    'Space-Regular': require('@/assets/fonts/SpaceMono-Regular.ttf')
  });


    return (
        <>
        <StatusBar style='auto' />
        <Stack initialRouteName="(tabs)/home">
            <Stack.Screen name="(tabs)/home" options={{ headerShown: false }} />
        </Stack>
        </>
    )
}
