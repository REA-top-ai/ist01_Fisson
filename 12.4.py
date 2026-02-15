oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print("Обновленный словарь Oscar winners:")
for category, winner in oscar_winners.items():
    print(f"{category}: {winner}")