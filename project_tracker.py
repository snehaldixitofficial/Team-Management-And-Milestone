A = {}
B = {}
C = {}

def work_create_new():
    print("\n\n--- Start a New Work ---")
    work_name_here = input("Name of work: ")
    topic_for_work = input("What is the topic: ")
    date_end = input("When must it finish (DD/MM/YYYY): ")

    A[work_name_here] = {
        "topic": topic_for_work,
        "finish_day": date_end,
        "the_team": [],
        "status_now": "Not started"
    }
    print(f"Work '{work_name_here}' is added to the system!")

def person_add_to_system():
    print("\n\n--- Put a Person on the Team ---")
    person_full_name = input("Person's full name: ")
    person_id = input("ID number: ")

    B[person_full_name] = {
        "id_num": person_id,
        "the_works": []
    }
    print(f"Person '{person_full_name}' is now in the people list!")

def link_person_to_work_function():
    print("\n\n--- Link Person to Work ---")
    
    print("Works you can use:")
    for work_name in A:
        print(f"- {work_name}")
    
    work_to_link = input("Which work name: ")
    person_to_link = input("Which person name: ")

    if work_to_link in A:
        if person_to_link in B:
            
            already_there = False
            for team_member in A[work_to_link]["the_team"]:
                if team_member == person_to_link:
                    already_there = True
            
            if not already_there:
                A[work_to_link]["the_team"].append(person_to_link)
            
            work_already_linked = False
            for personal_work in B[person_to_link]["the_works"]:
                if personal_work == work_to_link:
                    work_already_linked = True
            
            if not work_already_linked:
                B[person_to_link]["the_works"].append(work_to_link)

            print(f"{person_to_link} is now linked to {work_to_link}!")
        else:
            print("That person is not in the people list (system B)!")
    else:
        print("That work is not in the work list (system A)!")

def goal_make_new():
    print("\n\n--- Make a New Small Goal ---")

    print("Works you can use:")
    for work_name in A:
        print(f"- {work_name}")
    
    work_for_goal = input("Work name for this goal: ")
    goal_name = input("Give the goal's name: ")
    goal_day = input("When is the goal due (DD/MM/YYYY): ")

    if work_for_goal in A:
        key_for_goal = f"{work_for_goal}_{goal_name}"
        C[key_for_goal] = {
            "work_linked": work_for_goal,
            "goal_title": goal_name,
            "day_due": goal_day,
            "goal_state": "Need to do"
        }
        print(f"Goal '{goal_name}' is made for {work_for_goal}!")
    else:
        print("Work not found in system A!")

def goal_change_status():
    print("\n\n--- Change Goal Status ---")

    print("Goals available:")
    for key, goal_data in C.items():
        print(f"- {goal_data['goal_title']} ({goal_data['work_linked']}) - {goal_data['goal_state']}")
        
    goal_name_in = input("What is the goal name to change: ")
    work_name_in = input("What is the work name this goal belongs to: ")
    goal_key_find = f"{work_name_in}_{goal_name_in}"

    if goal_key_find in C:
        print("New status options: Need to do, Doing now, Done")
        new_word = input("Give new status: ")
        C[goal_key_find]["goal_state"] = new_word
        print(f"Goal status is changed to '{new_word}'!")
    else:
        print("Goal not found in system C!")

def work_view_one():
    print("\n\n--- Look at One Work's Info ---")

    print("Works you can view:")
    for work_name in A:
        print(f"- {work_name}")
    
    work_name = input("Which work name to view: ")

    if work_name in A:
        data = A[work_name]
        print(f"\nWork Name: {work_name}")
        print(f"Topic: {data['topic']}")
        print(f"Finish Date: {data['finish_day']}")
        print(f"Status: {data['status_now']}")

        print("\nTeam People:")
        if data["the_team"]:
            for person in data["the_team"]:
                print(f"- {person}")
        else:
            print("Nobody is on this team yet")

        print("\nSmall Goals:")

        work_goals = []
        for key in C.keys():
            g = C[key]
            if g["work_linked"] == work_name:
                work_goals.append(g)

        if work_goals:
            for goal in work_goals:
                print(f"- {goal['goal_title']} | Due: {goal['day_due']} | Status: {goal['goal_state']}")
        else:
            print("No goals for this work yet")
    else:
        print("Work not found!")

def all_work_view_function():
    print("\n\n--- View Everything ---")
    if A:
        for name, data in A.items():
            print(f"Work Name: {name}")
            print(f"  Topic: {data['topic']}")
            print(f"  Finish Date: {data['finish_day']}")
            print(f"  Team Size: {len(data['the_team'])}")
            print()
    else:
        print("No work in the system! Please add one.")

def work_delete_from_system():
    print("\n\n--- Take a Work Out of the System ---")

    print("Works available to delete:")
    for work_name in A:
        print(f"- {work_name}")
    
    project_to_get_rid_of = input("Which work name to take out: ")

    if project_to_get_rid_of in A:
        
        for person in A[project_to_get_rid_of]["the_team"]:
            if person in B:
                B[person]["the_works"].remove(project_to_get_rid_of)

        goals_to_remove = []
        for key in C.keys():
            goal = C[key]
            if goal["work_linked"] == project_to_get_rid_of:
                goals_to_remove.append(key)
        
        for goal_key in goals_to_remove:
            del C[goal_key]

        del A[project_to_get_rid_of]
        print(f"Work '{project_to_get_rid_of}' is gone from the system A!")
    else:
        print("Work not found in system A!")

def main_menu_run():
    while True:
        print("\n" + "="*50)
        print("THE MAIN MENU - PICK A NUMBER")
        print("="*50)
        print("1. Make Work")
        print("2. Add Person")
        print("3. Link Person to Work")
        print("4. Make Goal")
        print("5. Change Goal Status")
        print("6. Look at One Work")
        print("7. Look at All Works")
        print("8. Delete Work")
        print("9. Stop Program")
        print("-"*50)

        choice_num = input("Pick a number (1-9): ")

        if choice_num == "1":
            work_create_new()
        elif choice_num == "2":
            person_add_to_system()
        elif choice_num == "3":
            link_person_to_work_function()
        elif choice_num == "4":
            goal_make_new()
        elif choice_num == "5":
            goal_change_status()
        elif choice_num == "6":
            work_view_one()
        elif choice_num == "7":
            all_work_view_function()
        elif choice_num == "8":
            work_delete_from_system()
        elif choice_num == "9":
            print("Program finished.")
            break
        else:
            print("Wrong number! Try again with 1, 2, 3, etc.")

if __name__ == "__main__":
    main_menu_run()