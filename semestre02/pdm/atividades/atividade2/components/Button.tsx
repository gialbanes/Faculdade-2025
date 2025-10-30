import { useState } from "react";
import {
  Animated,
  Pressable,
  PressableProps,
  StyleSheet,
  Text,
  View,
} from "react-native";

type Variant = "primary" | "secondary" | "info" | "danger" | "success" | "outline";

type Props = PressableProps & {
  title: string;
  variant?: Variant;
  size?: "small" | "medium" | "large";
  fullWidth?: boolean;
  icon?: string;
};

export default function Button({ 
  title, 
  variant = "primary", 
  size = "medium",
  fullWidth = true,
  icon,
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
      case "secondary":
        return {
          button: styles.secondaryButton,
          text: styles.secondaryButtonText,
        };
      case "info":
        return {
          button: styles.infoButton,
          text: styles.infoButtonText,
        };
      case "danger":
        return {
          button: styles.dangerButton,
          text: styles.dangerButtonText,
        };
      case "success":
        return {
          button: styles.successButton,
          text: styles.successButtonText,
        };
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
          {icon && <Text style={[styles.icon, variantStyles.text]}>{icon}</Text>}
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
  icon: {
    marginRight: 8,
    fontSize: 18,
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
  secondaryButton: {
    backgroundColor: "#f8f9fa",
    borderWidth: 2,
    borderColor: "#6c757d",
  },
  secondaryButtonText: {
    color: "#6c757d",
  },
  outlineButton: {
    backgroundColor: "transparent",
    borderWidth: 2,
    borderColor: "#dc3545",
  },
  outlineButtonText: {
    color: "#dc3545",
  },
  infoButton: {
    backgroundColor: "#17a2b8",
    borderWidth: 2,
    borderColor: "#138496",
  },
  infoButtonText: {
    color: "#ffffff",
  },
  dangerButton: {
    backgroundColor: "#dc3545",
    borderWidth: 2,
    borderColor: "#c82333",
  },
  dangerButtonText: {
    color: "#ffffff",
  },
  successButton: {
    backgroundColor: "#28a745",
    borderWidth: 2,
    borderColor: "#1e7e34",
  },
  successButtonText: {
    color: "#ffffff",
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
