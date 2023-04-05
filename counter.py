def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    days ={}
    with open(file_name) as file:
        for line in file:
            if line.startswith("From "):
                line = line.strip()
                line = line.split()
                days[line[2]] = days.get(line[2], 0) + 1
    print(days)






## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
