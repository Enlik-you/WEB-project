import { Country } from '../interfaces/country';

export const MOCK_COUNTRIES: Country[] = [
  {
    id: 1,
    name: 'Canada',
    continent: 'North America',
    climateType: 'Cold',
    score: 88,
    reasons: [
      'High safety',
      'Strong healthcare',
      'Family-friendly environment'
    ],
    safetyScore: 9,
    healthcareScore: 9,
    educationScore: 9,
    jobMarketScore: 8,
    politicalStabilityScore: 9,
    familyFriendlinessScore: 9,
    averageCostLevel: 'High',
    officialLanguage: 'English, French',
    description: 'A safe and developed country with strong healthcare and education.'
  },
  {
    id: 2,
    name: 'Portugal',
    continent: 'Europe',
    climateType: 'Mild',
    score: 81,
    reasons: [
      'Lower cost of living',
      'Mild climate',
      'Good lifestyle balance'
    ],
    safetyScore: 8,
    healthcareScore: 8,
    educationScore: 7,
    jobMarketScore: 6,
    politicalStabilityScore: 8,
    familyFriendlinessScore: 8,
    averageCostLevel: 'Medium',
    officialLanguage: 'Portuguese',
    description: 'A calm European country with a pleasant climate and balanced lifestyle.'
  },
  {
    id: 3,
    name: 'Germany',
    continent: 'Europe',
    climateType: 'Mild',
    score: 80,
    reasons: [
      'Strong economy',
      'Good healthcare',
      'Stable political environment'
    ],
    safetyScore: 8,
    healthcareScore: 9,
    educationScore: 8,
    jobMarketScore: 9,
    politicalStabilityScore: 9,
    familyFriendlinessScore: 7,
    averageCostLevel: 'High',
    officialLanguage: 'German',
    description: 'A strong economy with reliable systems and solid career opportunities.'
  },
  {
    id: 4,
    name: 'Malaysia',
    continent: 'Asia',
    climateType: 'Warm',
    score: 78,
    reasons: [
      'Affordable living',
      'Warm climate',
      'Comfortable lifestyle'
    ],
    safetyScore: 7,
    healthcareScore: 7,
    educationScore: 7,
    jobMarketScore: 6,
    politicalStabilityScore: 7,
    familyFriendlinessScore: 8,
    averageCostLevel: 'Low',
    officialLanguage: 'Malay',
    description: 'An affordable country with warm weather and a comfortable day-to-day lifestyle.'
  },
  {
    id: 5,
    name: 'Japan',
    continent: 'Asia',
    climateType: 'Mild',
    score: 74,
    reasons: [
      'Very safe environment',
      'Strong infrastructure',
      'High quality services'
    ],
    safetyScore: 10,
    healthcareScore: 8,
    educationScore: 8,
    jobMarketScore: 7,
    politicalStabilityScore: 8,
    familyFriendlinessScore: 7,
    averageCostLevel: 'High',
    officialLanguage: 'Japanese',
    description: 'A highly organized country with strong safety and excellent infrastructure.'
  }
];