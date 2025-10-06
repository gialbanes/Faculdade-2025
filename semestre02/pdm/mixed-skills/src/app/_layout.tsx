import { Stack } from 'expo-router'; // abre as telas uma por cima da outra 

export default function RootLayout() {
    return (
        <Stack>
            <Stack.Screen name='onboarding' 
            // tira as configs padrões
            options={{headerShown: false}} /> 
        </Stack>
    )

}