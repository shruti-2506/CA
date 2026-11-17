"""
Practical No 1.1 -- Implementation of Intelligent Agent: Simple Reflex Agent
Title: AI-Based Smart Beach Cleaning Vacuum Cleaner
Author: Shruti Siddheshwar Thorat
Batch: A1 | Roll No: 16 | PRN: 202401040053
"""

import random

class BeachEnvironment:
    def __init__(self):
        # Different conditions that can be found on the beach
        self.beach = {
            'Zone A': 'Clean',
            'Zone B': 'Clean',
            'Zone C': 'Clean'
        }
        # Randomly place different objects
        conditions = ['Plastic', 'Seaweed', 'Sharp Object', 'Clean']
        for zone in self.beach:
            self.beach[zone] = random.choice(conditions)

class BeachCleaningVaccum:
    def __init__(self, environment):
        self.environment = environment
        # Starting score
        self.score = 0
        # Robot starts at a random zone
        self.current_zone = random.choice(list(environment.beach.keys()))
        print("========================================")
        print("          BEACH CLEANING ")
        print("========================================")
        print(f"\nInitial Beach Conditions:\n{self.environment.beach}")
        print(f"\nRobot starts at: {self.current_zone}")
        self.clean_beach()

    def clean_beach(self):
        zones = list(self.environment.beach.keys())
        for zone in zones:
            self.current_zone = zone
            print("\n" + "-"*40)
            print(f"Vaccum is at: {self.current_zone}")
            condition = self.environment.beach[self.current_zone]
            print(f"Condition found: {condition}")

            # Rule 1: Plastic
            if condition == 'Plastic':
                print("Plastic waste detected!")
                print("Action: Collecting plastic waste...")
                self.environment.beach[self.current_zone] = 'Clean'
                self.score += 2
                print("Plastic collected successfully.")
                print("Score +2")

            # Rule 2: Seaweed
            elif condition == 'Seaweed':
                print("Seaweed detected!")
                print("Action: Collecting seaweed...")
                self.environment.beach[self.current_zone] = 'Clean'
                self.score += 1
                print("Seaweed collected.")
                print("Score +1")

            # Rule 3: Sharp Object
            elif condition == 'Sharp Object':
                print("Sharp object detected!")
                print("Action: Avoiding the object...")
                self.score += 1
                print("Robot safely moved around it.")
                print("Score +1")

            # Rule 4: Clean zone
            else:
                print("Zone is already clean.")
                print("Action: Moving to the next zone.")

            # Move to next zone
            if zone != zones[-1]:
                print("Moving to the next beach zone...")

        # Final result
        self.show_result()

    def show_result(self):
        print("\n" + "="*40)
        print("          CLEANING COMPLETED")
        print("========================================")
        print(f"Final Beach Conditions:\n{self.environment.beach}")
        print(f"\nFinal Performance Score: {self.score}")
        if all(c == 'Clean' for z, c in self.environment.beach.items() if c != 'Sharp Object'):
            print("Beach cleaning task completed successfully!")

if __name__ == '__main__':
    # Create the beach environment
    beach = BeachEnvironment()
    # Create the cleaning robot
    robot = BeachCleaningVaccum(beach)
