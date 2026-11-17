# Practical 1.2: Reasoning in Knowledge-Based Expert System

**Title:** Food Recommendation Expert System Using Prolog  
**Author:** Shruti Siddheshwar Thorat  
**Batch:** A1 | **Roll No:** 16 | **PRN:** 202401040053  

---

## 📌 Aim
To develop a rule-based food recommendation system using Prolog that suggests suitable food items based on the user's taste, meal type, dietary preference, mood, and weather conditions.

---

## 🎯 Objectives
- Construct a declarative knowledge base containing culinary items and relational properties.
- Model expert domain knowledge using Prolog facts and inference rules.
- Support multi-criteria recommendations across:
  - **Meal Type:** Breakfast, Lunch, Dinner, Snack, Dessert
  - **Taste:** Spicy, Sweet, Cheesy, Salty, Healthy
  - **Dietary Preference:** Vegetarian, Non-vegetarian, Vegan
  - **Context:** Weather (Hot, Cold, Rainy) and Mood (Happy, Sad, Tired, Stressed, Energetic)
- Implement an interactive conversational loop (`FoodieBot`) utilizing pattern matching and recursion.

---

## 🧩 Knowledge Base Structure

### Facts
- `food(Item)`: Pizza, Biryani, Pasta, Dosa, Idli, Salad, Soup, Sandwich, Icecream, Pancake.
- `taste(Item, Taste)`: Relates food items to flavor profiles (e.g. `taste(biryani, spicy).`).
- `food_type(Item, Type)`: Diet classifications (`vegetarian`, `non_vegetarian`, `vegan`).
- `meal(Item, Meal)`: Appropriate meal time (`breakfast`, `lunch`, `dinner`, etc.).
- `weather_food(Weather, Item)`: Weather-influenced comfort food pairings.
- `mood_food(Mood, Item)`: Emotional state food mappings.

### Interactive Inference Queries
Users interact with `foodiebot` by inputting Prolog lists ending with a dot:
- `[hello].`
- `[what, can, you, do].`
- `[i, am, happy].`
- `[i, want, vegetarian, food].`
- `[i, want, healthy, food].`
- `[what, should, i, eat, for, dinner].`
- `[weather, is, rainy].`
- `[tell, me, about, pizza].`
- `[best, food, for, tired, when, weather, is, rainy].`
- `[bye].`

---

## 🚀 Execution Instructions

### Using SWI-Prolog
1. Start SWI-Prolog in this directory:
   ```bash
   swipl foodiebot.pl
   ```
2. Start the interactive chatbot:
   ```prolog
   ?- foodiebot.
   ```
3. Type queries as Prolog lists followed by a period (e.g., `[i, want, spicy, food].`).
4. Type `[bye].` to exit.
