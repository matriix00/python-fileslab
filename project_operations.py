from this import d
from data_check import chk_valid_date,chk_valid_details, chk_valid_int, chk_valid_st

last_edit=""

def create_project(id):
    title=chk_valid_st("please enter title of your project ")
    details=chk_valid_details("please enter project details ")
    total=chk_valid_int("please enter your total target ")
    start_date=chk_valid_date("Enter the start date in format 'dd/mm/yy' : ")
    end_date=chk_valid_date("Enter the end date in format 'dd/mm/yy' : ")
    user_id=id
    projects_data=f"{user_id}:{title}:{details}:{total}:{start_date}:{end_date}"
    # if create_project_file(projects_data):
    #     print("project created successfully ")
    return projects_data
    
    


def create_project_file(id):
    try:
        fileobject=open("projects.txt","a")
    except Exception as e :
        print(e)
        return False
    else:
        p=create_project(id)
        fileobject.write(p+"\n")
        return True


def listAll_projects():
    try:
        fileobject=open("projects.txt", "r")
    except Exception as e:
        print(e)
        return False
    else:
        projects= fileobject.readlines()
        return(projects)

def search_project_byID(id):
    allprojects=listAll_projects()
    for project in allprojects:
        project_details=project.split(":")
        if project_details[0]==id:
            project_index=allprojects.index(project)
            return project_index
    else:
        return False

def delete_project(id):
    project_index=search_project_byID(id)
    allprojects=listAll_projects()
    del allprojects[project_index]
    deleted=write_projects_on_file(allprojects)
    if deleted:
        print("project deleted successfully")
    print(allprojects)

def write_projects_on_file(projects):
    try:
        fileobject=open("projects.txt", "w")
    except Exception as e:
        print(e)
        return False
    else:
        fileobject.writelines(projects)
        return True


def edit_project(id):
    project_index=search_project_byID(id)
    allprojects=listAll_projects()
    if project_index and project_index == 0:
        project_data=create_project(id)
        print(project_data)

        updated_data=f"{id}:{project_data[0]}:{project_data[1]}:{project_data[2]}:{project_data[3]}:{project_data[4]}"
        allprojects[project_index]=updated_data
        update=write_projects_on_file(allprojects)
        return update







def search_project_byDate(date):
    allprojects=listAll_projects()
    for project in allprojects:
        project_details=project.split(":")
        if project_details[4]==date:
            project_index=allprojects.index(project)
            return project_index
    else:
        return False


