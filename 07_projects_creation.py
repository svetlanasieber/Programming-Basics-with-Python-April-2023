#	Името на архитекта - текст
#	Брой на проектите, които трябва да изготви - цяло число в интервала [0 … 100]
# Изготвянето на един проект отнема три часа

# "The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."

name_architect = input()
projects_numbers = int(input())
one_project = 3

needed_hours_for_projects = projects_numbers * one_project

print(f"The architect {name_architect} will need {needed_hours_for_projects} hours to complete {projects_numbers} project/s.")



# Лектор, примерно решение
#architect_name = input()
#projects_numbers = int(input())
# Отнема му  по 3 часа да изпълни един проект.
#print (f"The architect {architect_name} will need {projects_numbers * 3} hours to complete {projects_numbers} project/s.")