from lib_bitsen.simulate import simulate


# b1 = bit()
# print(b1.get_data())
# task = "COLLECTOR"
# b1.set_task(task)
# b1.cycle()
# print(b1.get_data())


speed = 1 # 1 speed = 1 sec / 60 speed = 60 sec

s = simulate(speed)
#s.simulate()
s.defaultstart()