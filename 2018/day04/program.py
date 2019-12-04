from pprint import pprint

HOURS = "000000000011111111112222222222333333333344444444445555555555"
MINUTES = "012345678901234567890123456789012345678901234567890123456789"


class Entry:
    def __init__(self, raw_text):
        self.time = raw_text.split(']')[0][1:]
        self.day = self.time.split('-')[1]+'-'+self.time.split('-')[2].split(' ')[0].strip()
        self.activity = raw_text.split(']')[1].strip()


def output_timings(days_info):
    header_str = (
        f"Date   ID  {HOURS}\n"
        f"           {MINUTES}"
    )
    print(header_str)

    for day in days_info:
        print(f"{day['date']} {day['guard_id']}   {''.join(day['minutes'])}")


def process_entry(entry, day_info):
    print(entry.activity)

    if "Guard" in entry.activity:
        entry.guard_id = entry.activity.split("#")[1].split(' ')[0]
    if "falls" in entry.activity:
        day_info

def process_entries(entries):
    sorted_entries = sorted(entries, key=lambda x: x.time)
    print(f"First date: {sorted_entries[0].time}")
    print(f"Last date: {sorted_entries[-1].time}")
    print(f"Found {len(entries)} entries to process.")

    days_info = []

    prev_day = None
    day_info = None
    active_guard = None

    for entry in sorted_entries:
        current_day = entry.day
        if current_day != prev_day:
            if prev_day:
                days_info.append(day_info)
            minutes = ['.'] * 60
            day_info = {
                'date': current_day,
                'minutes': minutes,
            }
        if active_guard:
            day_info['guard_id'] = active_guard

        process_entry(entry)
        if hasattr(entry, 'guard_id'):
            active_guard = entry.guard_id
            day_info['guard_id'] = entry.guard_id

        prev_day = current_day

    days_info.append(day_info)

    output_timings(days_info)


def work_entries():
    test_data = [
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ]

    test_entries = [Entry(line.strip()) for line in test_data]

    process_entries(test_entries)

    #input_file = "input.txt"
    #with open(input_file) as input:
        #entries = [Entry(line.strip()) for line in input]

    #process_entries(entries)

if __name__ == "__main__":
    work_entries()