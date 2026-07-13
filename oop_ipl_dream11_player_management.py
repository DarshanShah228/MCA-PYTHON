# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 20:17:44 2026

@author: darsh
"""

class Player:
    # Class variable (shared by all objects)
    total_players = 0

    # Constructor
    def __init__(self, name, team, role, credits, points_scored):
        self.name = name
        self.team = team
        self.role = role
        self.credits = credits
        self.points_scored = points_scored

        # Increment total players
        Player.total_players += 1

    # Method to return fantasy points
    def get_fantasy_points(self):
        return self.points_scored

    # String representation of object
    def __str__(self):
        return f"{self.name} ({self.team}) - {self.role} - {self.credits} Credits"


# Inheritance
class Captain(Player):

    # Constructor
    def __init__(self, name, team, role, credits, points_scored):
        super().__init__(name, team, role, credits, points_scored)

    # Method overriding (Polymorphism)
    def get_fantasy_points(self):
        return self.points_scored * 2


# ---------------- Driver Code ----------------

p1 = Player("Virat Kohli", "RCB", "Batsman", 10.5, 78)
p2 = Player("Bumrah", "MI", "Bowler", 9.0, 45)
c1 = Captain("Rohit Sharma", "MI", "Batsman", 9.5, 60)

print(p1)
print("Fantasy Points:", p1.get_fantasy_points())

print(p2)
print("Fantasy Points:", p2.get_fantasy_points())

print(c1)
print("Fantasy Points:", c1.get_fantasy_points())

print("Total Players:", Player.total_players)
