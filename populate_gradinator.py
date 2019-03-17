import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gradinator_project.settings')
import django

django.setup()
from gradinator.models import Course
from gradinator.models import Coursework


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models

    wad_coursework = [
        {"name": "rango",
         "course": "wad",
         "weight": 0.1},
        {"name": "quiz",
         "course": "wad",
         "weight": 0.1},
        {"name": "group project application",
         "course": "wad",
         "weight": 0.25},
        {"name": "group project design specification",
         "course": "wad",
         "weight": 0.1},
        {"name": "group project presentation",
         "course": "wad",
         "weight": 0.05},
        {"name": "exam",
         "course": "wad",
         "weight": 0.4}

    ]

    courses = {"wad": {"name": "wad",
                       "id": "COMPSCI2021",
                       "url": "https://www.gla.ac.uk/coursecatalogue/course/?code=COMPSCI2021",
                       "taught_by": "David Manlove",
                       "description": "The aim of this course is to provide students with a comprehensive overview of web application development. It will provide students with the skills to design and develop distributed web applications in a disciplined manner, using a range of tools and technologies. It will also strengthen their understanding of the context and rationale of distributed systems. ",
                       "requirements_of_entry": "Entry to Level 2 Computing Science is guaranteed to students who achieve a GPA of B3 or better in their level 1 courses at the first sitting. All others would be at the discretion of the School.All grades for Computing Science courses must be at D3 or better at either attempt. Strong python skills are a requirement for this course.",
                       "credits": 10,
                       "year": 2,
                       "school": "School of Computing Science",
                       "coursework": wad_coursework,
                       "slug": "wad"}, }

    # If you want to add more courses or coursework
    # add them to the dictionaries above

    # The code below goes through the course dictionary, then adds each course,
    # and then adds all the associated pages for that category.
    for course, course_data in courses.items():

        c = add_course(course_data["name"], course_data["id"], course_data["url"], course_data["taught_by"],
                       course_data["description"],
                       course_data["requirements_of_entry"], course_data["credits"], course_data["year"],
                       course_data["school"])
        for cw in course_data["coursework"]:
            add_coursework(c, cw["name"], cw["weight"])

    # Print out the courses we have added.
    for c in Course.objects.all():
        for cw in Coursework.objects.filter(course=c):
            print("- {0} - {1}".format(str(c), str(cw)))


def add_coursework(course, name, weight):
    cw = Coursework.objects.get_or_create(course=course, name=name)[0]
    cw.course = course
    cw.name = name
    cw.weight = weight
    cw.save()
    return cw


def add_course(name, id, url, taught_by,description,
               requirements_of_entry, course_credits, year,
               school):
    c = Course.objects.get_or_create(id=id)[0]
    c.name = name
    c.id = id
    c.url = url
    c.taught_by = taught_by
    c.description = description
    c.requirements_of_entry = requirements_of_entry
    c.credits = course_credits
    c.year = year
    c.school = school
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Gradinator population script...")
    populate()
