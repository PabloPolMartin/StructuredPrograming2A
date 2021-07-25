import sys

if __name__ == "__main__":
    for month in range(1,13):
        print(f"\nMes:", month)
        if month==2:
            for day in range(1,29):
                print("Dia:", day)
        elif month== 4:
            for day in range(1,31):
                print("Dia:", day)
        elif month == 6:
            for day in range(1,31):
                print("Dia:", day)
        elif month == 9:
            for day in range(1,31):
                print("Dia:", day)
        elif month == 11:
            for day in range(1,31):
                print("Dia", day)
        else:
            for day in range(1,32):
                print("Dia", day)