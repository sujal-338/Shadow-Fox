justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial team:", justice_league)

print("Number of members:", len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman as leader:", justice_league)

justice_league.remove("Superman")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Superman")
print("Separated Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team assembled:", justice_league)

justice_league.sort()
print("Sorted team:", justice_league)
print("New leader:", justice_league[0])
