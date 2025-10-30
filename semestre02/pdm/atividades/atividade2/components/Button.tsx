import { useState } from "react";
import {
  Animated,
  Pressable,
  PressableProps,
  StyleSheet,
  Text,
  View,
} from "react-native";

type Variant = "primary" | "outline";

type Props = PressableProps & {
  title: string;
  variant?: Variant;
  size?: "small" | "medium" | "large";
  fullWidth?: boolean;
};

export default function Button({ 
  title, 
  variant = "primary", 
  size = "medium",
  fullWidth = true,
  ...rest 
}: Props) {
  const [scaleAnim] = useState(new Animated.Value(1));
  const [opacityAnim] = useState(new Animated.Value(1));

  const handlePressIn = () => {
    Animated.parallel([
      Animated.timing(scaleAnim, {
        toValue: 0.95,
        duration: 150,
        useNativeDriver: true,
      }),
      Animated.timing(opacityAnim, {
        toValue: 0.8,
        duration: 150,
        useNativeDriver: true,
      })
    ]).start();
  };

  const handlePressOut = () => {
    Animated.parallel([
      Animated.timing(scaleAnim, {
        toValue: 1,
        duration: 150,
        useNativeDriver: true,
      }),
      Animated.timing(opacityAnim, {
        toValue: 1,
        duration: 150,
        useNativeDriver: true,
      })
    ]).start();
  };

  const getVariantStyles = () => {
    switch (variant) {
      case "outline":
        return {
          button: styles.outlineButton,
          text: styles.outlineButtonText,
        };
      default:
        return {
          button: styles.primaryButton,
          text: styles.primaryButtonText,
        };
    }
  };

  const getSizeStyles = () => {
    switch (size) {
      case "small":
        return {
          button: styles.smallButton,
          text: styles.smallText,
        };
      case "large":
        return {
          button: styles.largeButton,
          text: styles.largeText,
        };
      default:
        return {
          button: styles.mediumButton,
          text: styles.mediumText,
        };
    }
  };

  const variantStyles = getVariantStyles();
  const sizeStyles = getSizeStyles();

  // Remove shadow for transparent buttons
  const shouldHaveShadow = variant !== "outline";

  return (
    <Pressable onPressIn={handlePressIn} onPressOut={handlePressOut} {...rest}>
      <Animated.View
        style={[
          styles.button,
          !shouldHaveShadow && styles.noShadow,
          variantStyles.button,
          sizeStyles.button,
          fullWidth && styles.fullWidth,
          {
            transform: [{ scale: scaleAnim }],
            opacity: opacityAnim,
          },
        ]}
      >
        <View style={styles.content}>
          <Text style={[styles.buttonText, variantStyles.text, sizeStyles.text]}>
            {title}
          </Text>
        </View>
      </Animated.View>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  button: {
    borderRadius: 12,
    justifyContent: "center",
    alignItems: "center",
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 3,
    },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 5,
  },
  noShadow: {
    shadowOpacity: 0,
    elevation: 0,
  },
  fullWidth: {
    width: "100%",
  },
  content: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
  },
  buttonText: {
    fontWeight: "600",
    textAlign: "center",
  },
  // Variants
  primaryButton: {
    backgroundColor: "#0077b5",
    borderWidth: 2,
    borderColor: "#005582",
  },
  primaryButtonText: {
    color: "#ffffff",
  },
  outlineButton: {
    backgroundColor: "transparent",
    borderWidth: 2,
    borderColor: "#dc3545",
  },
  outlineButtonText: {
    color: "#dc3545",
  },
  // Sizes
  smallButton: {
    paddingVertical: 8,
    paddingHorizontal: 16,
    minHeight: 36,
  },
  mediumButton: {
    paddingVertical: 12,
    paddingHorizontal: 24,
    minHeight: 48,
  },
  largeButton: {
    paddingVertical: 16,
    paddingHorizontal: 32,
    minHeight: 56,
  },
  smallText: {
    fontSize: 14,
  },
  mediumText: {
    fontSize: 16,
  },
  largeText: {
    fontSize: 18,
  },
});
