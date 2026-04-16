export interface Country {
    id: number;
    name: string;
    continent: string;
    climateType: string;
    score: number;
    reasons: string[];
    safetyScore: number;
    healthcareScore: number;
    educationScore: number;
    jobMarketScore: number;
    politicalStabilityScore: number;
    familyFriendlinessScore: number;
    averageCostLevel: string;
    officialLanguage: string;
    description: string;
  }