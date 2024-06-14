import csv
import os
import sys

def draw():
    print(">--------------------<")

def menu():
    draw()
    print("1. Create new database.")
    print("2. Visit old database.")
    print("3. Quit.")
    draw()

def entry():
    while True:
        try:
            srno = int(input("Enter the Serial number of the data: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    name = input("Enter the name of item: ")
    while True:
        try:
            price = float(input("Enter the price of item: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    return srno, name, price

def new_databaseopts():
    fname = input("Enter the name of the database you want to create: ")
    with open(f"{fname}.csv", 'w', newline='') as fc:
        draw()
        print("File created!!")
        draw()
        enames = ["Sr. no.", "Name", "Price"]
        writer = csv.writer(fc)
        writer.writerow(enames)
        while True:
            draw()
            print("a. Enter new data.")
            print("b. Remove an entry.")
            print("c. Back [<--]")
            draw()
            ans = input("What do you want to do? (a/b/c) ")
            if ans == 'a':
                draw()
                n = int(input("How many entries do you want to make? "))
                for _ in range(n):
                    srno, name, price = entry()
                    writer.writerow([srno, name, price])
            elif ans == 'b':
                print("Remove functionality is not implemented yet.")
            elif ans == 'c':
                break

def visit_old_database():
    fname_old = input("Enter the name of the database you want to open: ")
    if not os.path.exists(f"{fname_old}.csv"):
        print(f"File {fname_old}.csv not found. Please try again.")
        return
    while True:
        draw()
        print("I. Show Data.")
        print("II. Add New Entry.")
        print("III. Remove Entry.")
        print("IV. Back [<--]")
        draw()
        inp = input("What do you want to do? (I/II/III/IV) ").upper()
        if inp == 'I':
            with open(f"{fname_old}.csv", 'r') as fo:
                reader = csv.reader(fo)
                for row in reader:
                    print(row)
        elif inp == 'II':
            with open(f"{fname_old}.csv", 'a', newline='') as fo:
                writer = csv.writer(fo)
                srno, name, price = entry()
                writer.writerow([srno, name, price])
        elif inp == 'III':
            temp_fname = f"{fname_old}_temp.csv"
            with open(f"{fname_old}.csv", 'r') as fo, open(temp_fname, 'w', newline='') as temp_file:
                reader = csv.reader(fo)
                writer = csv.writer(temp_file)
                rows = list(reader)
                writer.writerows(rows)
                srno_to_remove = input("Enter the Serial number of the entry to remove: ")
                writer.writerows(row for row in rows if row[0] != srno_to_remove)
            os.replace(temp_fname, f"{fname_old}.csv")
            print(f"Entry with Serial number {srno_to_remove} removed.")
        elif inp == 'IV':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        menu()
        reply = input("What do you want to do? (1/2/3) ")
        if reply == '1':
            new_databaseopts()
        elif reply == '2':
            visit_old_database()
        elif reply == '3':
            sys.exit()

if __name__ == "__main__":
    main()

