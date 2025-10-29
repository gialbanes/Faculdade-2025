import AsyncStorage from '@react-native-async-storage/async-storage';
import { Profile } from "@/types/profile";

const PROFILE_STORAGE_KEY = 'user_profile';

export class ProfileStorage {

    static async load(): Promise<Profile | null> {
        const profileJson = await AsyncStorage.getItem(PROFILE_STORAGE_KEY);

        if (! profileJson) {
            return null;
        }

        const profile: Profile = JSON.parse(profileJson);
        return profile;
    }

    static async save(profile: Profile): Promise<void> {
        const profileJson = JSON.stringify(profile);
        await AsyncStorage.setItem(PROFILE_STORAGE_KEY, profileJson);
    }
}