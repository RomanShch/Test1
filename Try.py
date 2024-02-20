import json
import os
from datetime import datetime




def create_note(file_name):
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    note_id = len(notes) + 1

    note_title = input("Введите заголовок заметки ")

    note_body = input("Введите текст заметки ")

    note = {
        "id": note_id,

        "title": note_title,

        "body": note_body,
        
        "timestamp": timestamp
    }

    notes.append(note)

    save_notes(file_name)




def show_all():

    for note in notes:
        print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nТекст: {note['body']}\nДата/Время: {note['timestamp']}\n")






def change_note(file_name:str):
    note_id = int(input("Введите ID заметки, которую хотите отредактировать "))
    note_index = -1

    for index, note in enumerate(notes):
        if note['id'] == note_id:
            note_index = index
            break


    if note_index != -1:
        note_title = input("Введите новый заголовок заметки: ")
        
        note_body = input("Введите новый текст заметки: ")

        notes[note_index]['title'] = note_title

        notes[note_index]['body'] = note_body

        notes[note_index]['timestamp'] = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

        save_notes(file_name)
        print("Заметка успешно отредактирована")

    else:
        print("Заметка с указанным ID не найдена")



def delete_note(file_name):
    note_id = int(input("ВВедите ID заметки, которую хотите удалить"))

    note_index = -1

    for index, note in enumerate(notes):
        if note['id'] == note_id:
            note_index = index
            break

    if note_index != -1:
        del notes[note_index]
        save_notes(file_name)  
        print("Заметка успешно удалена")
    else:
        print("Заметка с указанным ID не найдена")          



def save_notes(file_name:str):
    with open(file_name, "w", encoding ="utf-8") as file:
        json.dump(notes,file,ensure_ascii=False)



def load_notes(file_name:str):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding ="utg-8") as file:
            notes.extend(json.load(file))

file_name = "notes.json"

notes = []
load_notes(file_name)






def main():
        
        file_name = "notes.json"
        flag_exit = False
        while not flag_exit:
            print('1 - показать все заметки')
            print('2 - добавление заметки')
            print('3 - удаление заметки')
            print('4 - редактирование заметки')
            print('5 - выход')
            answer = input('Введите необходимую операцию ')
            if answer == '1':
                show_all()
            elif answer == '2':
                create_note(file_name)   
            elif answer == '3':
                delete_note(file_name)
            elif answer == '4':
                change_note(file_name)  
            elif answer == '5':
                flag_exit = True
            else :
                print('Введите корректую операцию') 


if __name__== '__main__':
     main()