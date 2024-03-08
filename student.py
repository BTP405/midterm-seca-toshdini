"""
Module for defining Student class.

This module provides a class for representing students, their enrolled courses, and grades.
"""


class Student:
    """
    A class to represent a student.

    Attributes:
        name (str): The name of the student.
        student_id (int): The unique ID of the student.
        enrolled_courses (list): A list of courses the student is enrolled in.
        grades (dict): A dictionary to store grades for courses and assessments.

    Methods:
        enroll_course(course): Enrolls the student in a course.
        drop_course(course): Drops a course from the student's enrollment.
        submit_grade(course, assessment, grade): Submits a grade for a student in a course.
    """

    def __init__(self, name, student_id):
        """
        Initializes a Student object with a name and an ID.

        Args:
            name (str): The name of the student.
            student_id (int): The unique ID of the student.
        """
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []
        self.grades = {}


    def enroll_course(self, course):
        """
        Enrolls the student in a course if prerequisites are met.

        Args:
            course (Course): The course object to be enrolled in.

        Returns:
            None
        """
        if course in self.enrolled_courses:
            print(f"{self.name} is already enrolled in {course.course_name}.")
        else:
            prerequisites_met = True
            if course.prerequisites:
                for prerequisite in course.prerequisites:
                    if prerequisite not in self.enrolled_courses:
                        prerequisites_met = False
                        print(f"{self.name} has not completed the prerequisite course {prerequisite.course_name}.")
                        break
            if prerequisites_met:
                if len(course.enrolled_students) < course.sections:
                    course.enrolled_students.append(self)
                    self.enrolled_courses.append(course)
                    print(f"{self.name} has enrolled in {course.course_name}.")
                else:
                    course.waitlisted_students.append(self)
                    print(f"{self.name} has been added to the waitlist for {course.course_name}.")
        

    def drop_course(self, course):
        """
        Drops a course from the student's enrollment.

        Args:
            course (Course): The course object to be dropped.

        Returns:
            None
        """
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            course.enrolled_students.remove(self)
            print(f"{self.name} has dropped {course.course_name}.")
        elif course in course.waitlisted_students:
            course.waitlisted_students.remove(self)
            print(f"{self.name} has been removed from the waitlist for {course.course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course.course_name}.")


    def submit_grade(self, course, assessment, grade):
        """
        Submits a grade for a student in a course.

        Args:
            course (Course): The course object.
            assessment (str): The assessment name.
            grade (float): The grade for the assessment.

        Returns:
            None
        """
        if course in self.enrolled_courses:
            if course.course_name not in self.grades:
                self.grades[course.course_name] = {}
            self.grades[course.course_name][assessment.assessment_type] = grade
            print(f"{self.name} submitted a grade of {grade} for {assessment.assessment_type} in {course.course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course.course_name}.")