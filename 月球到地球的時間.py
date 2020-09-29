dist=384400
speed=1225
total_hours=dist//1225
days=total_hours//24
hours=total_hours%24
#days,hours=divmod(total_hours,24)
print('需要',days,'天，又',hours)
