    # Task 1
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
    # Task 2
entertainment = "audio system" if attendees > 100 else "projector"
print(entertainment)
    # Task 3
diet = input("What are your dietary needs? (vegetarian/non-vegetarian): ")
catering = "Veggie Delight Caterers" if diet == "vegetarian" else "Gourmet Meals Caterers"
print(catering)
