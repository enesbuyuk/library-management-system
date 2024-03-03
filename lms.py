class Library:
    def __init__(self, filename, type_of_opening_file):
        self.filename = filename
        self.type_of_opening_file = type_of_opening_file
        self.file = open(self.filename, self.type_of_opening_file)

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book = line.strip().split(",")
            print(f"Book: {book[0]}, Author: {book[1]}", )

    def add_book(self):
        try:
            title_input = input("Enter the book title: ").strip()
            author_input = input("Enter the author: ").strip()
            year_input = input("Enter the release year: ").strip()
            pages_input = input("Enter the number of pages: ").strip()
            try:
                year = int(year_input)
                pages = int(pages_input)
            except ValueError:
                print("Please enter valid integers for pages and the release year.")
                return
            self.file.write(f"{title_input},{author_input},{year},{pages}\n")
            print(f"Book '{title_input}' by {author_input} added successfully.")

        except Exception:
            print("The book was not successfully added.")

    def remove_book(self):
        title_to_remove = input("Enter the book title to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        new_lines = [line for line in lines if title_to_remove.strip() != line.strip().split(",")[0]]
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(new_lines)
        print(f"Book '{title_to_remove}' removed successfully.")

    def show_menu(self):
        while True:
            print("\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\nQ) Quit")
            choice = input("Enter your choice (Press 'q/Q' to quit.): ")
            if choice == "1":
                self.list_books()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.remove_book()
            elif choice == "q" or choice == "Q":
                print("Exiting the menu. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


lib = Library("books.txt", "a+")
lib.show_menu()
