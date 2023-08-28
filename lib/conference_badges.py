def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    # badges = []
    # for name in names:
    #     badges.append(badge_maker(name))
    # return badges
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    # welcome_msgs_with_rooms = []
    # for index, name in enumerate(names):
    #     welcome_msgs_with_rooms.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
    # return welcome_msgs_with_rooms
    return [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(names)]


def printer(names):
    for name in names:
        print(badge_maker(name))
    for message in assign_rooms(names):
        print (message)
