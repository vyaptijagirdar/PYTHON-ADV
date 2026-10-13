import numpy as np

heart_rate = np.random.randint(880,151,10)

print("heart rates for 10 mins :")
print(heart_rate)

first_5_minutes= heart_rate[:5]

print("\nheart rate during first 5 minutes: ")
print(first_5_minutes)

maximum = np.max(heart_rate)
minimum = np.min(heart_rate)
average = np.mean(heart_rate)

print("\nmaximum heart rate:",maximum,"BPM")
print("minimum heart rate",minimum,"BPM")
print("average heart rate:",round(average,2),"BPM")

high_rate = heart_rate >120

print("\nheart rates exceeding 120 BPM: ")
print(heart_rate[high_rate])

minutes = np.where(heart_rate > 120)[0] + 1

print("\n minutes where heart rate exceeded 120 BPM: ")
print(minutes)
