grade_book = {}
while True:
  user_choice = input("Pick an option (add, view or exit): ")
  if user_choice == "add":
   course = input("Enter course code (e.g., MTH101): ").upper().strip()
   score = int(input("Enter the score (0-100): "))
   grade_book[course] = score
   print(f"Added {course} with a score of {score}")
  elif user_choice == "view":
   print(grade_book)
  elif user_choice == "exit":
   break
  else:
    print("Invalid choice pick add, view or exit")

