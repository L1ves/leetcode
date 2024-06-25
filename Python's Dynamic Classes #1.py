"""Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:

- Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!

Tim sighed, he already knew it's gonna be a long day.
Few hours later, boss came again:
Much better - he said - but now I want to change that class name to SecondUsefulClass,

and went off. Although Timmy had no idea why changing name is so important for his boss, he realized, that it's not the end, so he turned to you, his guru, to help him and asked you to prepare some function, which could change name of given class.
Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), but starting only with upper case letter. In other case it should raise an exception.
Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that, that Timmy yet has to learn them.

"""

import re


def class_name_changer(cls, new_name):
    if not re.match(r'[A-Z][a-zA-Z0-9]*$', new_name):
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name
    return cls



# def class_name_changer(cls, new_name):
#     assert new_name[0].isupper() and new_name.isalnum()
#     cls.__name__ = new_name