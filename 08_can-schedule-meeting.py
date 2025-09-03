"""
Create a function `can_schedule_meeting` that takes a string startTime in "HH:MM" format
and a number durationMinutes.

The function should return True if the meeting starts and ends within the working
hours of 07:30 to 17:45, otherwise return False.

Examples:

Input:  startTime = "07:30", durationMinutes = 30
Output: True

Input:  startTime = "07:00", durationMinutes = 60
Output: False

Input:  startTime = "17:00", durationMinutes = 30
Output: True

Input:  startTime = "17:30", durationMinutes = 20
Output: False

Input:  startTime = "09:15", durationMinutes = 120
Output: True

Input:  startTime = "16:50", durationMinutes = 60
Output: False
"""


def get_total_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


def can_schedule_meeting(start_time, duration):
    meeting_starts = get_total_minutes(start_time)
    meeting_ends = meeting_starts + duration
    day_starts = get_total_minutes("07:30")
    day_ends = get_total_minutes("17:45")

    return (meeting_starts >= day_starts) and (meeting_ends <= day_ends)


print(can_schedule_meeting("07:30", 30) == True)  # starts at opening, ends within hours
print(can_schedule_meeting("07:00", 60) == False)  # starts before opening
print(can_schedule_meeting("17:00", 30) == True)  # ends exactly at closing
print(can_schedule_meeting("17:30", 20) == False)  # starts after closing
print(can_schedule_meeting("09:15", 120) == True)  # well within hours
print(can_schedule_meeting("16:50", 60) == False)  # would end after closing
print(can_schedule_meeting("12:00", 0) == True)  # zero-length meeting, valid
print(can_schedule_meeting("07:30", 0) == True)  # zero-length, starts at opening
print(can_schedule_meeting("17:45", 0) == True)  # zero-length, at closing
