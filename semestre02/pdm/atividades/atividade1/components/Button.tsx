import { useState } from "react";
import {
    Animated,
    Pressable,
    PressableProps,
    StyleSheet,
    Text,
    View,
} from "react-native";

type Variant = "primary" | "secondary" | "info";

type Props = PressableProps & {
  title: string;
  variant?: Variant;
};

export default function Button({ title, variant = "primary", ...rest }: Props) {
  const [pressAnim] = useState(new Animated.Value(1));

  const handlePressIn = () => {
    Animated.timing(pressAnim, {
      toValue: 0.95,
      duration: 100,
      useNativeDriver: true,
    }).start();
  };

  const handlePressOut = () => {
    Animated.timing(pressAnim, {
      toValue: 1,
      duration: 100,
      useNativeDriver: true,
    }).start();
  };

  const buttonVariantStyle =
    variant === "secondary"
      ? styles.secondaryButton
      : variant === "info"
      ? styles.infoButton
      : styles.primaryButton;
  const buttonTextVariantStyle =
    variant === "secondary"
      ? styles.secondaryButtonText
      : variant === "info"
      ? styles.infoButtonText
      : styles.primaryButtonText;

  return (
    <Pressable onPressIn={handlePressIn} onPressOut={handlePressOut} {...rest}>
      <Animated.View 
        style={[
          styles.buttonWrapper,
          {
            transform: [{ scale: pressAnim }],
          },
        ]}
      >
        <View style={[styles.button, buttonVariantStyle]}>
          <Text style={[styles.buttonText, buttonTextVariantStyle]}>
            {title}
          </Text>
        </View>
      </Animated.View>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  buttonWrapper: {
    width: "100%",
    height: 50,
    borderRadius: 25,
  },
  button: {
    width: "100%",
    height: 50,
    borderRadius: 25,
    justifyContent: "center",
    alignItems: "center",
    paddingHorizontal: 20,
    elevation: 3,
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
  },
  primaryButton: {
    backgroundColor: "#007bff",
  },
  secondaryButton: {
    backgroundColor: "#6c757d",
  },
  infoButton: {
    backgroundColor: "#17a2b8",
  },
  buttonText: {
    fontSize: 16,
    fontWeight: "600",
    textAlign: "center",
    color: "#ffffff",
  },
  primaryButtonText: {
    color: "#ffffff",
  },
  secondaryButtonText: {
    color: "#ffffff",
  },
  infoButtonText: {
    color: "#ffffff",
  },
});
