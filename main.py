
todo_list = []


def menu():

    while True:    
        print('***Main Menu***')
        print('1. Add New Task')
        print('2. View All Task')
        print('3. Remove a Task')
        print('4. Mark As Done')
        print('5. Exit')
    
        choice = input('Enter your choice: ')
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            print('Exiting...')
            exit()
        else:
            print('Invalid choice. Please try again.')

def add_task():
    task = input('Enter a new task: ')
    todo_list.append(task)
    print(f'{task} - Pending')
    
def view_task():
    print('***Task List***')
    for task in todo_list:
        print(task)

def remove_task():
    task = input('Enter a task to remove: ')
    if task in todo_list:
        todo_list.remove(task)
        print(f'{task} - Removed')
    else:
        print(f'{task} - Not found')
        
def mark_done():
    task = input('Enter a task to mark as done: ')
    


    
menu()