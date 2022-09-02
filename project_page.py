from project_operations import search_project_byDate,edit_project,delete_project, search_project_byID,create_project_file, listAll_projects
def project(userID):
    choice=input("""
    c =>>>>> create new project
    l =>>>>> list all projects
    e =>>>>> edit project
    d =>>>>> delete project
    s =>>>>> search for a project 
    """)

    if choice in ['c','l','e','d','s']:
        if choice == 'c':
            create_project_file(userID)
        elif choice == 'l':
            print(listAll_projects())
        elif choice == 'e':
            edit_project(userID)
        elif choice =='d':
            delete_project(userID)
        else:
            print(search_project_byDate())
