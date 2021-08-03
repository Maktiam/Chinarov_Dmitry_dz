duration = 1000000
day = duration // 86400
hours = (duration % 86400) // 3600
min = ((duration % 86400) % 3600) // 60
sek = ((duration % 86400) % 3600) % 60
print(day,'дн.', hours,'час.', min,'мин.', sek,'сек.')





