total = 100
done = 0

while done < total:
    print("Do 10 jumping jacks")
    done = done + 10
    if done >= total:
        break
    tired = input("Are you tired? ")
    tired = tired.lower()
    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? ")
        skip = skip.lower()
        if skip == "yes" or skip == "y":
            break
    print("Jumping jacks remaining:", total - done)

if done >= total:
    print("Congratulations! You completed the workout")
else:
    print("You completed a total of", done, "jumping jacks")
