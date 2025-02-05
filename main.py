import psycopg2
import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("Choose what type of graph you would like to see")
    print("1. Line graph")
    print("2. Bar graph")
    print("3. Pie chart")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Line graph")
    elif choice == "2":
        print("Bar graph")
    elif choice == "3":
        print("Pie chart")  
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()
