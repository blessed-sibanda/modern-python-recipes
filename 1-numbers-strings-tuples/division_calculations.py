total_seconds = 7385

# Floor division
hours, remaining_seconds = divmod(total_seconds, 3600)
minutes, seconds = divmod(remaining_seconds, 60)
print(hours, minutes, seconds)

# True division
hours = total_seconds / 3600
print(round(hours, 4))