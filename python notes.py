import csv
import datetime

notes = []

def create_note():
    note_id = len(notes) + 1
    note_name = input("Введите заголовок заметки: ")
    note_text = input("Введите текст заметки: ")
    note_created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_last_edited_time = note_created_time
    notes.append({"id": note_id, "name": note_name, "text": note_text, 
                  "created_time": note_created_time, "last_edited_time": note_last_edited_time})
    with open("notes.csv", mode="a", newline="", encoding="utf-8") as notes_file:
        writer = csv.writer(notes_file)
        writer.writerow([note_id, note_name, note_text, note_created_time, note_last_edited_time])
    print(f"Заметка {note_id} создана.")

def show_notes():
    with open("notes.csv", mode="r", encoding="utf-8") as notes_file:
        reader = csv.reader(notes_file)
        next(reader) 
        for row in reader:
            note_id, note_name, note_text, note_created_time, note_last_edited_time = row
            note_created_time = datetime.datetime.strptime(note_created_time, "%Y-%m-%d %H:%M:%S")
            note_last_edited_time = datetime.datetime.strptime(note_last_edited_time, "%Y-%m-%d %H:%M:%S")
            if note_created_time > datetime.datetime.now() - datetime.timedelta(days=7): 
                print(f"{note_id} ; {note_name} ; {note_text} ; {note_created_time} ; {note_last_edited_time}")

def view_note():
    note_id = int(input("Введите ID заметки: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        print(f"{note['name']}\n{note['text']}\nLast edited: {note['last_edited_time']}")
    else:
        print("Заметка не найдена.")

def edit_note():
    note_id = int(input("Введите ID заметки: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        new_text = input("Введите новый текст: ")
        note["text"] = new_text
        note["last_edited_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("notes.csv", mode="w", newline="", encoding="utf-8") as notes_file:
            writer = csv.writer(notes_file)
            writer.writerow(["id", "name", "text", "created_time", "last_edited_time"]) 
            for note in notes:
                writer.writerow([note["id"], note["name"], note["text"], 
                                  note["created_time"], note["last_edited_time"]])
        print(f"Заметка {note_id} удалена.")
    else:
        print("Заметка не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        notes.remove(note)
        with open("notes.csv", mode="w", newline="", encoding="utf-8") as notes_file:
            writer = csv.writer(notes_file)
            writer.writerow(["id", "name", "text", "created_time", "last_edited_time"]) 
            for note in notes:
                writer.writerow([note["id"], note["name"], note["text"], 
                                  note["created_time"], note["last_edited_time"]])
        print(f"Заметка {note_id} удалена.")
    else:
        print("Заметка не найдена.")

def main():
    with open("notes.csv", mode="r", encoding="utf-8") as notes_file:
        reader = csv.reader(notes_file)
        next(reader) 
        for row in reader:
            note_id, note_name, note_text, note_created_time, note_last_edited_time = row
            note_created_time = datetime.datetime.strptime(note_created_time, "%Y-%m-%d %H:%M:%S")
            note_last_edited_time = datetime.datetime.strptime(note_last_edited_time, "%Y-%m-%d %H:%M:%S")
            notes.append({"id": int(note_id), "name": note_name, "text": note_text, 
                          "created_time": note_created_time, "last_edited_time": note_last_edited_time})

    while True:
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Просмотр заметки")
        print("4. Изменение заметки")
        print("5. Удаление заметки")
        print("6. Выход")
        choice = input("Введите команду: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            view_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            break
        else:
            print("Ошибка ввода команды.")

if __name__ == "__main__":
    main()
