import os

def run_selected_main():
    data_folder = 'Data'


    folders_in_data = [d for d in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, d))]
    print("Доступні роботи:")
    print("\n".join(folders_in_data))


    selected_folder = input("Виберіть лабораторну: ")


    if selected_folder in folders_in_data:
        folder_path = os.path.join(data_folder, selected_folder)
        main_path = os.path.join(folder_path, 'main.py')


        if os.path.exists(main_path):
            os.system(f'python {main_path}')
        else:
            print(f"main.py not found in {folder_path}")
    else:
        print("Введено некоректну назву папки.")


run_selected_main()
