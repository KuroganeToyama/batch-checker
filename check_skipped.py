import os
import re
import argparse
import time

os.chdir("...")

special_pattern = r"Regex for files you don't want the script to care about"
staff = ["List of staff"]

def count_sub(assn, type, list_flag):
    students = []
    if type == "...":
        handin = "..."
        for student in os.listdir(handin):
            if (re.match(special_pattern, student) is None) and (student not in staff):
                students.append(student)
        print("...")
        if list_flag:
            print(students)
            
    elif type == "...":
        handin = "..."
        for student in os.listdir(handin):
            if (re.match(special_pattern, student) is None) and (student not in staff):
                students.append(student)
        print("...")
        if list_flag:
            print(students)

def check_skipped(assn, type, list_flag):
    target_html = ""
    if type == "...":
        target_html = "..."
    elif type == "...":
        target_html = "..."

    students_with_sub = []
    students_without_sub = []

    for student in os.listdir():
        # If student doesn't have the html, check if student has made any submissions 
        # and record if they have (i.e. batch mode skipped them)
        if (re.match(special_pattern, student) is None) and (student not in staff) and (target_html not in os.listdir(student)):
            if type == "...":
                handin_type1 = "..."
                type1_check = (student in os.listdir(handin_type1)) and \
                                ("..." in os.listdir(handin_type1 + f"{student}/"))
                if type1_check:
                    students_with_sub.append(student)
                elif (student in os.listdir(handin_type1)):
                    students_without_sub.append(student)
            
            elif type == "...":
                handin_type2 = "..."
                type2_check = (student in os.listdir(handin_type2)) and \
                                "..." in os.listdir(handin_type2 + f"{student}/")
                if type2_check:
                    students_with_sub.append(student)
                elif (student in os.listdir(handin_type2)):
                    students_without_sub.append(student)

    # Feel free to say whatever you want here
    print("\n")
    print(f"Found {str(len(students_with_sub))} students ...")

    if type == "...":
        print(f"Found {str(len(students_without_sub))} students ...")
        print("\n")
    elif type == "...":
        print(f"Found {str(len(students_without_sub))} students ...")
        print("\n")
    
    if list_flag:
        print("...")
        print(students_with_sub)
        print("\n")
        print("...")
        print(students_without_sub)
        print("\n")

def check_skipped_updated(assn, type, list_flag, start_time, end_time):
    skipped_students = []
    all_students = []

    target_html = ""
    if type == "...":
        target_html = "..."
    elif type == "...":
        target_html =  "..."

    for student in os.listdir():
        if (re.match(special_pattern, student) is None) and (student not in staff) and (target_html in os.listdir(student)):
            all_students.append(student)
            html_path = f"{os.getcwd()}/{student}/{target_html}"
            modified_time = os.path.getmtime(html_path)
            if not (start_time <= modified_time <= end_time):
                skipped_students.append(student)

    # Again, feel free to say whatever you want here
    print("\n")
    print(f"Found {str(len(all_students))} students ...")
    print(f"Found {str(len(skipped_students))} students ...")
    print("\n")
    
    if list_flag:
        print(skipped_students)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Check for skipped students")

    parser.add_argument("assn", type = str, help = "Assignment number")
    parser.add_argument("type", choices = ["List of types of test"], type = str, help = "Types of test")
    parser.add_argument("-verbose", "-v", action = "store_true", help = "List the found students")

    parser.add_argument("start_time", type = str, nargs = '?', help = "Start timestamp (format: 'YYYY-MM-DD HH:MM:SS')")
    parser.add_argument("end_time", type = str, nargs = '?', help = "End timestamp (format: 'YYYY-MM-DD HH:MM:SS')")

    args = parser.parse_args()
    assn = args.assn
    type = args.type
    verbose = args.verbose
    start_time = None if args.start_time is None else time.mktime(time.strptime(args.start_time, "%Y-%m-%d %H:%M:%S")) 
    end_time = None if args.end_time is None else time.mktime(time.strptime(args.end_time, "%Y-%m-%d %H:%M:%S"))

    count_sub(assn, type, verbose)

    if start_time is None and end_time is None:
        check_skipped(assn, type, verbose)
    elif start_time is not None and end_time is not None:
        check_skipped_updated(assn, type, verbose, start_time, end_time)