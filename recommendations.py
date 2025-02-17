from enum import Enum
import random
 
class StressLevel(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    SEVERE = "severe"
 
class StressRecommendations:
    def __init__(self):
        self.breathing_exercises = {
            "Box Breathing": "Inhale for 4 counts, hold for 4, exhale for 4, hold for 4. Repeat.",
            "4-7-8 Breathing": "Inhale for 4 counts, hold for 7, exhale for 8 counts.",
            "Deep Belly Breathing": "Place hand on belly, breathe deeply making your belly rise and fall.",
            "Alternate Nostril Breathing": "Alternate breathing through left and right nostrils.",
            "Progressive Relaxation": "Tense and relax each muscle group progressively."
        }

        self.physical_activities = {
            "low": [
                "Take a gentle 10-minute walk",
                "Basic stretching exercises",
                "Light gardening",
                "Gentle yoga poses",
                "Short walk around your workspace"
            ],
            "moderate": [
                "30-minute brisk walk",
                "Bike ride",
                "Swimming",
                "Dynamic stretching",
                "Dancing to favorite music"
            ],
            "high": [
                "High-intensity workout",
                "Running",
                "Boxing exercise",
                "Jump rope",
                "Competitive sports"
            ]
        }

        self.mindfulness_activities = {
            "low": [
                "5-minute meditation",
                "Mindful observation of surroundings",
                "Gratitude journaling",
                "Mindful walking",
                "Body scan meditation"
            ],
            "moderate": [
                "15-minute guided meditation",
                "Mindful drawing or coloring",
                "Nature meditation",
                "Progressive muscle relaxation",
                "Mindful eating practice"
            ],
            "high": [
                "30-minute deep meditation",
                "Yoga nidra",
                "Extended journaling session",
                "Visualization exercises",
                "Sound bath meditation"
            ]
        }

        self.lifestyle_changes = {
            "low": [
                "Take regular breaks during work",
                "Maintain a consistent sleep schedule",
                "Stay hydrated throughout the day",
                "Practice digital detox for 30 minutes",
                "Organize your workspace"
            ],
            "moderate": [
                "Establish a morning routine",
                "Create a balanced daily schedule",
                "Set boundaries with work and personal time",
                "Improve sleep hygiene",
                "Regular meal times"
            ],
            "high": [
                "Seek professional counseling",
                "Join stress management workshops",
                "Consider work-life balance adjustments",
                "Create a support system",
                "Regular health check-ups"
            ]
        }

        self.social_support = {
            "low": [
                "Call a friend for a quick chat",
                "Share your feelings with family",
                "Join online communities",
                "Participate in group activities",
                "Connect with colleagues"
            ],
            "moderate": [
                "Schedule regular social activities",
                "Join support groups",
                "Plan social gatherings",
                "Engage in team sports or group exercises",
                "Regular family meetings"
            ],
            "high": [
                "Seek professional counseling",
                "Join therapy groups",
                "Regular support group meetings",
                "Family therapy sessions",
                "Build a strong support network"
            ]
        }

    def _get_stress_level(self, stress_score):
        """
        Determine stress level based on stress score
        """
        if stress_score < 0.3:
            return StressLevel.LOW
        elif stress_score < 0.6:
            return StressLevel.MODERATE
        elif stress_score < 0.8:
            return StressLevel.HIGH
        else:
            return StressLevel.SEVERE

    def _get_immediate_actions(self, stress_level):
        """
        Provide immediate actions based on stress level
        """
        immediate_actions = {
            StressLevel.LOW: [
                "Take a few deep breaths",
                "Stretch at your desk",
                "Drink some water",
                "Take a short break"
            ],
            StressLevel.MODERATE: [
                "Step outside for fresh air",
                "Do a quick breathing exercise",
                "Call a friend",
                "Listen to calming music"
            ],
            StressLevel.HIGH: [
                "Find a quiet space",
                "Practice box breathing",
                "Call your support person",
                "Use a stress relief app"
            ],
            StressLevel.SEVERE: [
                "Contact a mental health professional",
                "Use crisis helpline if needed",
                "Reach out to your support system",
                "Remove yourself from stressful situation if possible"
            ]
        }
        return random.sample(immediate_actions[stress_level], 2)

    def generate_recommendations(self, stress_score):
        """
        Generate comprehensive recommendations based on stress score
        
        Args:
            stress_score (float): A value between 0 and 1 indicating stress level
        
        Returns:
            dict: Structured recommendations
        """
        stress_level = self._get_stress_level(stress_score)
        intensity = stress_level.value

        # Select appropriate recommendations based on stress level
        recommendations = {
            "stress_level": stress_level.value,
            "immediate_actions": self._get_immediate_actions(stress_level),
            "breathing_exercise": random.choice(list(self.breathing_exercises.values())),
            "physical_activity": random.choice(self.physical_activities[intensity if intensity != "severe" else "high"]),
            "mindfulness": random.choice(self.mindfulness_activities[intensity if intensity != "severe" else "high"]),
            "lifestyle_change": random.choice(self.lifestyle_changes[intensity if intensity != "severe" else "high"]),
            "social_support": random.choice(self.social_support[intensity if intensity != "severe" else "high"])
        }

        # Add urgency note for severe cases
        if stress_level == StressLevel.SEVERE:
            recommendations["urgent_notice"] = (
                "Your stress levels appear to be severe. Consider speaking with a mental health "
                "professional or counselor. If you're having thoughts of self-harm, please contact "
                "emergency services or a crisis helpline immediately."
            )

        return recommendations

    def get_detailed_plan(self, stress_score):
        """
        Generate a detailed daily plan based on stress level
        
        Args:
            stress_score (float): A value between 0 and 1 indicating stress level
        
        Returns:
            dict: Structured daily plan
        """
        recommendations = self.generate_recommendations(stress_score)
        stress_level = recommendations["stress_level"]

        morning_routine = [
            "Start with deep breathing exercises",
            "Light stretching or yoga",
            "Healthy breakfast",
            "Review your day's priorities"
        ]

        afternoon_routine = [
            "Take regular breaks",
            "Practice mindfulness during lunch",
            "Short walk if possible",
            "Stay hydrated"
        ]

        evening_routine = [
            "Wind down activities",
            "Limited screen time",
            "Relaxation exercises",
            "Regular sleep schedule"
        ]

        return {
            "stress_level": stress_level,
            "morning_routine": morning_routine,
            "afternoon_routine": afternoon_routine,
            "evening_routine": evening_routine,
            "specific_recommendations": recommendations
        }

# Example usage
if __name__ == "__main__":
    recommender = StressRecommendations()
    
    # Test different stress levels
    test_scores = [0.2, 0.5, 0.7, 0.9]
    
    for score in test_scores:
        print(f"\nTesting stress score: {score}")
        recommendations = recommender.generate_recommendations(score)
        print("\nRecommendations:")
        for key, value in recommendations.items():
            print(f"{key}: {value}")
        
        print("\nDetailed Plan:")
        plan = recommender.get_detailed_plan(score)
        print("Morning Routine:", plan["morning_routine"])
        print("Afternoon Routine:", plan["afternoon_routine"])
        print("Evening Routine:", plan["evening_routine"])
