import csv

FILENAME = "eglsheet.csv"

with open(FILENAME, "r", newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

for row in rows:
    if row[3] == 'Borrowed':
        print(row)
        
name = input("enter your name: ").strip()
phone = input("enter phone number: ").strip()
email = input("enter ashoka email: ").strip()
game = input("enter game name: ").strip()




updated = False

for row in rows:
    if len(row) < 10:
        continue

    if row[1] == game:
        if row[3] != "Available":
            print("game is not available")
            break

        row[3] = "Borrowed"

        if row[4] == "":
            row[4] = name
            row[5] = phone
            row[6] = email
        else:
            row[7] = name
            row[8] = phone
            row[9] = email

        updated = True
        break

if updated:
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("borrow successful")
else:
    print("game not found")
