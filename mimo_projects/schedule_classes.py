def schedule_classes(classes, times):
    schedule = []

    index = 0
    while index < len(classes):
        scheduled_class = classes[index] + ": " + times[index]
        schedule.append(scheduled_class)
        index += 1

    return schedule 