registered_course = []

while True:
  student_choice = input("Choose an option (add, view, exit): ")
  if student_choice == "add":
    new_courz = input("Enter your course: ")
    registered_course.append(new_courz)
    print(f"Successfully added! your current list: {registered_course}")
  elif student_choice == "view":
    if registered_course == []:
      print("Your registry is empty.")
    else:
      print(f"Your registered courses: {registered_course}")
  elif student_choice == "exit":
    break
  else:
    print("Invalid option please choose add, view, or exit")
