from App.models import Staff
from App.database import db
from flask import jsonify

def get_staff(id):
    staff=Staff.query.get(id)
    if staff:
        return staff
    return None

def get_all_staff():
    return Staff.query.all()

def get_all_staff_json():
    staff = get_all_staff()
    if not staff:
        return None
    staff = [staf.toJSON() for staf in staff]
    return staff

def get_all_staff_notifs_json():
    staff = get_all_staff()
    if not staff:
        return None
    staff = [staf.toJSON_with_notifications() for staf in staff]
    return staff

def get_staff_by_firstName(firstName):
    staff= Staff.query.filter_by(firstName=firstName).all()
    staff = [staf.toJSON() for staf in staff]
    if staff==[]:
        return None
    return jsonify(staff)

def get_staff_by_lastName(lastName):
    staff=Staff.query.filter_by(lastName=lastName).all()
    staff = [staf.toJSON() for staf in staff]
    if staff == []:
        return None
    return jsonify(staff)

def get_staff_by_name(firstName, lastName):
    staff=Staff.query.filter_by(firstName=firstName, lastName=lastName).all()
    staff = [staf.toJSON() for staf in staff]
    if staff == []:
        return None
    return jsonify(staff)

def search_staff(type, keyword):
    if (type=="ID"):
        staff = get_staff(keyword)
        return staff.toJSON()
    else:
        if (type=="name"):
            name=keyword.split(",")
            return get_staff_by_name(name[0], name[1])
        if (type=="firstName"):
            return get_staff_by_firstName(keyword)
        if (type=="lastName"):
            return get_staff_by_lastName(keyword)
    return None

def get_staff_feed(staffID):
    staff = get_staff(staffID)
    return staff.notificationFeed

# get the notification feed for the current user
def get_staff_feed_json(staffID):
    notifs = get_staff_feed(staffID)
    if notifs:
        return [notif.toJSON() for notif in notifs]
    return None

