"""
Module for defining Instructor class.

This module provides a class for representing instructors and their assigned courses.
"""

class Instructor:
    """
    A class to represent an instructor.

    Attributes:
        name (str): The name of the instructor.
        instructor_id (int): The unique ID of the instructor.
        assigned_courses (list): A list of courses assigned to the instructor.

    Methods:
        assign_course(course): Assigns a course to the instructor.
    """

    def __init__(self, name, instructor_id):
        """
        Initializes an Instructor object with a name and an ID.

        Args:
            name (str): The name of the instructor.
            instructor_id (int): The unique ID of the instructor.
        """
        self.name = name
        self.instructor_id = instructor_id
        self.assigned_courses = []


    def assign_course(self, course):
        """
        Assigns a course to the instructor.

        Args:
            course (Course): The course object to be assigned.

        Returns:
            None
        """
        self.assigned_courses.append(course)


