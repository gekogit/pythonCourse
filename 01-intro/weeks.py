minutesInSevenWeeks = 60*24*7
print("\nSeven weeks contains ", minutesInSevenWeeks, " minutes.")

getSkillTimeNeeds = 75
myWeeklyLearningTime = 5.5


print(f'According to "https://python-ritaly.netlify.app/python_quickstart.html#zadania" for the new skill you need {getSkillTimeNeeds} learning hours.')
print(f'Spending {myWeeklyLearningTime} hours weekly, the new skill will appear after {getSkillTimeNeeds//myWeeklyLearningTime} weeks and {getSkillTimeNeeds%myWeeklyLearningTime} hours.')
