import json
import random
from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def fix_marks(name):
    schoolkid = get_child(name)
    child_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in child_bad_marks:
        mark.points = 4
        mark.save()


def delete_chastisements(name):
    schoolkid = get_child(name)
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def get_commendation_texts(filename):
    with open(filename, 'r') as f:
        commendation_texts = json.loads(f.read())
    return commendation_texts


def get_child(name):
    try:
        child = Schoolkid.objects.filter(full_name__contains=name).get()
    except ObjectDoesNotExist:
        print(f"There is no schoolkid with {name} name")
        return None
    except MultipleObjectsReturned:
        print(f"Request {name} returned multiple objects")
        return None
    return child


def create_commendation(name, lesson):
    commend = random.choice(get_commendation_texts('commend.json'))
    child = get_child(name)
    if not child:
        return None
    last_lesson = Lesson.objects.filter(year_of_study=child.year_of_study,
                                        group_letter=child.group_letter,
                                        subject__title=lesson).order_by('-date')[0]
    Commendation.objects.create(text=commend,
                                created=last_lesson.date,
                                schoolkid=child,
                                subject=last_lesson.subject,
                                teacher=last_lesson.teacher)


if __name__ == "__main__":
    commends = get_commendation_texts('commend.json')
