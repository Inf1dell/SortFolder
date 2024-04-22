from tkinter import *
import tkinter.filedialog
import os
import shutil


def choose_folder():
    global folder_path
    folder_selected = tkinter.filedialog.askdirectory()
    folder_path.set(folder_selected)


def get_file_format(filename):
    return filename.split('.')[-1]


def sort_files():
    selected_folder = folder_path.get()
    photo_checked = photo_var.get()
    video_checked = video_var.get()
    sound_checked = sound_var.get()
    zip_checked = zip_var.get()
    exe_checked = exe_var.get()
    pdf_checked = pdf_var.get()
    apk_checked = apk_var.get()

    graph_checked = graph_var.get()
    doc_checked = doc_var.get()
    exel_checked = exel_var.get()
    ppt_checked = ppt_var.get()
    text_checked = text_var.get()



    if not os.path.exists(selected_folder):
        result = "Папка не найдена"
    else:
        if selected_folder and (photo_checked or video_checked or sound_checked or zip_checked or exe_checked or pdf_checked or apk_checked or graph_checked or doc_checked or exel_checked or ppt_checked or text_checked):
            if photo_checked:
                os.makedirs(os.path.join(selected_folder, "Photos ALL"), exist_ok=True)
            if video_checked:
                os.makedirs(os.path.join(selected_folder, "Videos ALL"), exist_ok=True)
            if sound_checked:
                os.makedirs(os.path.join(selected_folder, "Sound ALL"), exist_ok=True)
            if zip_checked:
                os.makedirs(os.path.join(selected_folder, "Archives ALL"), exist_ok=True)
            if exe_checked:
                os.makedirs(os.path.join(selected_folder, "Executables ALL"), exist_ok=True)
            if pdf_checked:
                os.makedirs(os.path.join(selected_folder, "PDF ALL"), exist_ok=True)
            if apk_checked:
                os.makedirs(os.path.join(selected_folder, "APK ALL"), exist_ok=True)
            if graph_checked:
                os.makedirs(os.path.join(selected_folder, "Graph ALL"), exist_ok=True)
            if doc_checked:
                os.makedirs(os.path.join(selected_folder, "Document ALL"), exist_ok=True)
            if exel_checked:
                os.makedirs(os.path.join(selected_folder, "Exel ALL"), exist_ok=True)
            if ppt_checked:
                os.makedirs(os.path.join(selected_folder, "PPT ALL"), exist_ok=True)
            if text_checked:
                os.makedirs(os.path.join(selected_folder, "Text ALL"), exist_ok=True)

            for file_name in os.listdir(selected_folder):
                file_format = get_file_format(file_name)
                if photo_checked and file_format.lower() in ['jpg', 'jpeg', 'png', 'iso', 'svg', 'webp']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Photos ALL"))
                if video_checked and file_format.lower() in ['mp4', 'avi', 'mkv']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Videos ALL"))
                if sound_checked and file_format.lower() in ['mp3']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Sound ALL"))
                if zip_checked and file_format.lower() in ['zip', 'rar', '7z']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Archives ALL"))
                if exe_checked and file_format.lower() in ['exe', 'msi', 'torrent']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Executables ALL"))
                if pdf_checked and file_format.lower() in ['pdf']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "PDF ALL"))
                if apk_checked and file_format.lower() in ['apk']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "APK ALL"))

                if graph_checked and file_format.lower() in ['psd', 'fig', 'ai']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Graph ALL"))
                if doc_checked and file_format.lower() in ['doc', 'docx']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Document ALL"))
                if exel_checked and file_format.lower() in ['xls', 'xlsx']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Exel ALL"))
                if ppt_checked and file_format.lower() in ['ppt', 'pptx']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "PPT ALL"))
                if text_checked and file_format.lower() in ['txt', 'html', 'css', 'json', 'py']:
                    shutil.move(os.path.join(selected_folder, file_name), os.path.join(selected_folder, "Text ALL"))
            result = "Успешно"
        else:
            result = "Файлы формата отсутствуют"

    result_label.config(text=result)
root = Tk()
root.title("File Sorter")
root.geometry("500x200")
root.resizable(width=False, height=False)

folder_path = StringVar()
photo_var = IntVar()
video_var = IntVar()
sound_var = IntVar()
zip_var = IntVar()
exe_var = IntVar()
pdf_var = IntVar()
apk_var = IntVar()

graph_var = IntVar()
doc_var = IntVar()
exel_var = IntVar()
ppt_var = IntVar()
text_var = IntVar()


Label(root, text="Выберите папку для сортировки:").pack()

Entry(root, textvariable=folder_path).place(relx=0.02, rely=0.12, relwidth=0.65)
Button(root, text="Выбрать папку", command=choose_folder).place(relx=0.70, rely=0.1, relwidth=0.25)

Checkbutton(root, text="Фото", variable=photo_var).place(relx=0.02, rely=0.22)
Checkbutton(root, text="Видео", variable=video_var).place(relx=0.02, rely=0.32)
Checkbutton(root, text="Звук", variable=sound_var).place(relx=0.02, rely=0.42)
Checkbutton(root, text="Архивы", variable=zip_var).place(relx=0.02, rely=0.52)
Checkbutton(root, text="EXE", variable=exe_var).place(relx=0.02, rely=0.62)
Checkbutton(root, text="PDF", variable=pdf_var).place(relx=0.02, rely=0.72)
Checkbutton(root, text="APK", variable=apk_var).place(relx=0.02, rely=0.82)

Checkbutton(root, text="Графика", variable=graph_var).place(relx=0.25, rely=0.22)
Checkbutton(root, text="Документы", variable=doc_var).place(relx=0.25, rely=0.32)
Checkbutton(root, text="Таблицы", variable=exel_var).place(relx=0.25, rely=0.42)
Checkbutton(root, text="Презентации", variable=ppt_var).place(relx=0.25, rely=0.52)
Checkbutton(root, text="Текстовые", variable=text_var).place(relx=0.25, rely=0.62)

result_label = Label(root, text="")
result_label.place(relx=0.3, rely=0.9)

Button(root, text="Отсортировать", command=sort_files).place(relx=0.78, rely=0.8)

root.mainloop()