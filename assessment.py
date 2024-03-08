"""
Module for defining Assessment class.

This module provides a class for representing assessments.
"""

class Assessment:
    """
    A class to represent an assessment.

    Attributes:
        assessment_type (str): The type of assessment.

    Methods:
        None
    """
    

    def __init__(self, assessment_type):
        """
        Initializes an Assessment object with a type.

        Args:
            assessment_type (str): The type of assessment.
        """
        self.assessment_type = assessment_type
