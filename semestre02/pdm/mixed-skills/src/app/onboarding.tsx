import { Button, Text, View, StyleSheet } from "react-native";
import React, { useState } from "react";

// array com os passos do onboarding
const onboardingSteps = [
    {
        title: 'Explore trilhas',
        subtitle: 'Descubra trilhas de aprendizado personalizadas para suas necessidades.',
    },
    {
        title: 'Resolva desafios',
        subtitle: 'Supere obstáculos e teste suas habilidades.',
    },
    {
        title: 'Crie e compartilhe',
        subtitle: 'Crie e compartilhe seu próprio conteúdo de aprendizado.',
    },
    {
        title: 'Explore cursos',
        subtitle: 'Descubra cursos de aprendizado personalizados para suas necessidades.',
    },
]

export default function OnboardingScren() {
    // estado para controlar o passo atual do onboarding
    // estado no react funciona de forma que quando ele muda, a tela é re-renderizada
    // useState é um hook do react que permite criar estados em componentes funcionais
    const [step, setStep] = useState(0);

    // função para avançar para o próximo passo do onboarding 
    const handleNext = () => {
        if(step < onboardingSteps.length - 1) {
            setStep(step + 1);
        } else {
            // home
        }
    }
    return(
        <View style={styles.container}>
            <View style={styles.content}>
                <Text style={styles.title}>{onboardingSteps[step].title}</Text>
                <Text style={styles.subtitle}>{onboardingSteps[step].subtitle}</Text>
            </View>
            <View>
                <Button 
                title={step === onboardingSteps.length - 1 ? 'COMEÇAR' : 'PRÓXIMO'}
                onPress={handleNext}
                />
                <Button title="PULAR"/>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
        backgroundColor: '#ffffff',
      },
      content: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20
      },
      logo: {
        width: 150,
        height: 150,
        resizeMode: 'contain',
        marginBottom: 40,
    },
      footer: {
        width: '100%',
        gap:12,
        paddingBottom: 40,
      },
      title: {
        fontSize: 32,
        fontWeight: 'bold',
        marginBottom: 10,
        textAlign: 'center',
        color: '#112437'
      },
      subtitle: {
        fontSize: 18,
        color: '#4a4a4a',
        textAlign: 'center',
        marginBottom: 30,
      }
});
