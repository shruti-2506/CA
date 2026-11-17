/* =========================================================
   PRACTICAL ASSIGNMENT 1.2: REASONING IN KNOWLEDGE BASED EXPERT SYSTEM
   Food Recommendation Expert System Using Prolog
   Author: Shruti Siddheshwar Thorat
   PRN: 202401040053 | Roll No: 16 | Batch: A1
   ========================================================= */

/* KNOWLEDGE BASE */

/* FOOD INFORMATION */
food(pizza).
food(biryani).
food(pasta).
food(dosa).
food(idli).
food(salad).
food(soup).
food(sandwich).
food(icecream).
food(pancake).

/* FOOD TASTE */
taste(pizza, cheesy).
taste(biryani, spicy).
taste(pasta, cheesy).
taste(dosa, salty).
taste(idli, healthy).
taste(salad, healthy).
taste(soup, healthy).
taste(sandwich, salty).
taste(icecream, sweet).
taste(pancake, sweet).

/* FOOD TYPE */
food_type(pizza, vegetarian).
food_type(biryani, non_vegetarian).
food_type(pasta, vegetarian).
food_type(dosa, vegetarian).
food_type(idli, vegetarian).
food_type(salad, vegan).
food_type(soup, vegetarian).
food_type(sandwich, vegetarian).
food_type(icecream, vegetarian).
food_type(pancake, vegetarian).

/* MEAL INFORMATION */
meal(pizza, dinner).
meal(biryani, lunch).
meal(pasta, dinner).
meal(dosa, breakfast).
meal(idli, breakfast).
meal(salad, lunch).
meal(soup, dinner).
meal(sandwich, snack).
meal(icecream, dessert).
meal(pancake, breakfast).

/* WEATHER BASED FOOD */
weather_food(hot, salad).
weather_food(hot, icecream).
weather_food(cold, soup).
weather_food(cold, pasta).
weather_food(rainy, soup).
weather_food(rainy, dosa).

/* MOOD BASED FOOD */
mood_food(happy, pizza).
mood_food(happy, icecream).
mood_food(sad, icecream).
mood_food(sad, soup).
mood_food(tired, pasta).
mood_food(tired, soup).
mood_food(stressed, salad).
mood_food(stressed, soup).
mood_food(energetic, sandwich).
mood_food(energetic, dosa).

/* DYNAMIC LIST FOR RANDOM RESPONSES */
:- dynamic confuse/1.
confuse([
    'Sorry, I did not understand.',
    'Please tell me what you want to eat.',
    'Let me think about that.',
    'I have a tasty suggestion for you.'
]).

/* START FOODIEBOT */
foodiebot :-
    write('Hello! I am FoodieBot.'), nl,
    write('Your personal food recommendation chatbot.'), nl, nl,
    foodiebot_loop.

/* FOODIEBOT LOOP */
foodiebot_loop :-
    write('FoodieBot:- '),
    read(Input),
    reply(Input).

/* HELLO */
reply([hello | _]) :-
    write('Hello! Nice to meet you.'), nl, nl,
    foodiebot_loop.

reply([hi | _]) :-
    write('Hi! What would you like to eat today?'), nl, nl,
    foodiebot_loop.

/* ASK WHAT FOODIEBOT CAN DO */
reply([what, can, you, do | _]) :-
    write('I can recommend food based on your mood, taste,'), nl,
    write('meal, diet and weather.'), nl, nl,
    foodiebot_loop.

/* RECOMMEND FOOD BASED ON MOOD */
reply([i, am, Mood | _]) :-
    mood_food(Mood, Food),
    write('Since you are '),
    write(Mood),
    write(', I recommend '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* RECOMMEND FOOD BASED ON WEATHER */
reply([weather, is, Weather | _]) :-
    weather_food(Weather, Food),
    write('Since the weather is '),
    write(Weather),
    write(', you can try '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* RECOMMEND FOOD BASED ON TASTE */
reply([i, want, Taste, food | _]) :-
    taste(Food, Taste),
    write('I recommend '),
    write(Food),
    write(' because it is '),
    write(Taste),
    write('.'), nl, nl,
    foodiebot_loop.

/* FIND VEGETARIAN FOOD */
reply([i, want, vegetarian, food | _]) :-
    food_type(Food, vegetarian),
    write('You can try '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* FIND HEALTHY FOOD */
reply([i, want, healthy, food | _]) :-
    taste(Food, healthy),
    write('A healthy choice for you is '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* FIND SWEET FOOD */
reply([i, want, sweet, food | _]) :-
    taste(Food, sweet),
    write('For something sweet, try '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* FIND SPICY FOOD */
reply([i, want, spicy, food | _]) :-
    taste(Food, spicy),
    write('If you want something spicy, try '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* FIND BREAKFAST */
reply([what, should, i, eat, for, breakfast | _]) :-
    meal(Food, breakfast),
    write('For breakfast, I recommend '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* FIND LUNCH */
reply([what, should, i, eat, for, lunch | _]) :-
    meal(Food, lunch),
    write('For lunch, I recommend '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* FIND DINNER */
reply([what, should, i, eat, for, dinner | _]) :-
    meal(Food, dinner),
    write('For dinner, I recommend '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* FIND FOOD USING MOOD AND WEATHER */
reply([best, food, for, Mood, when, weather, is, Weather | _]) :-
    mood_food(Mood, Food),
    weather_food(Weather, Food),
    write('The best match I found is '),
    write(Food),
    write('.'), nl, nl,
    foodiebot_loop.

/* CHECK FOOD */
reply([is, Food, vegetarian | _]) :-
    food_type(Food, vegetarian),
    write('Yes, '),
    write(Food),
    write(' is vegetarian.'), nl, nl,
    foodiebot_loop.

/* FOOD INFORMATION */
reply([tell, me, about, Food | _]) :-
    food(Food),
    taste(Food, Taste),
    food_type(Food, Type),
    meal(Food, Meal),
    write(Food),
    write(' is a '),
    write(Taste),
    write(' '),
    write(Type),
    write(' food suitable for '),
    write(Meal),
    write('.'), nl, nl,
    foodiebot_loop.

/* BYE */
reply([bye | _]) :-
    write('It was nice helping you choose your food!'), nl,
    write('FoodieBot says: Enjoy your meal! Bye!'), nl.

/* RANDOM REPLY IF QUERY IS NOT UNDERSTOOD */
reply([_ | _]) :-
    retract(confuse([Next | Rest])),
    append(Rest, [Next], NewList),
    asserta(confuse(NewList)),
    write(Next), nl, nl,
    foodiebot_loop.
