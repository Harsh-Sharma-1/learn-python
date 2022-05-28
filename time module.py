import time

# find computer epoch time
print(time.ctime(0))

# return current seconds since epoch
print(time.time())


# to get the current time
print(time.ctime(time.time()))

# another method to get the current time
time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)


time_string = "20 April, 2020"
time_object_2 = time.strptime(time_string, "%d %B, %Y")
print(time_object_2)


time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string_2 = time.asctime(time_tuple)
print(time_string_2)


time_tuple_2 = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string_3 = time.mktime(time_tuple)
print(time_string_3)
