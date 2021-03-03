import time


class RocketEngine:
    count = 0
    all_power = 0

    def __init__(self, name, power):
        RocketEngine.count += 1
        self.name = name
        self.power = power
        self.working = False

    def start(self):
        if self.working:
            return
        RocketEngine.all_power += self.power
        self.working = True

    def stop(self):
        if not self.working:
            return
        RocketEngine.all_power -= self.power
        self.working = False

    def __str__(self):
        return f"Name: {self.name}, Power: {self.power}, Working: {self.working}"

    def __del__(self):
        self.stop()
        RocketEngine.count -= 1

    @staticmethod
    def status():
        print(f"Ilośc wszystkich silników: {RocketEngine.count}")
        print(f"Suma mocy silników: {RocketEngine.all_power}")



print("Ruszam...")
start_engines = [RocketEngine("start1", 50), RocketEngine("start2", 50)]
for engine in start_engines:
    engine.start()

time.sleep(0.5)
RocketEngine.status()

time.sleep(1)
print("Rozpędzam...")
acceleration_engines = [RocketEngine("acceleration1", 500), RocketEngine("acceleration2", 500)]
for engine in acceleration_engines:
    engine.start()

time.sleep(0.5)
RocketEngine.status()

time.sleep(1)
print("Włączam hipernapęd...")
hiper_engines = [RocketEngine("hiper1", 400000), RocketEngine("hiper2", 400000)]
for engine in hiper_engines:
    engine.start()

time.sleep(0.5)
RocketEngine.status()

time.sleep(1.5)
print("Wyłaczam hipernapęd...")
for engine in hiper_engines:
    engine.stop()
    engine.__del__()

time.sleep(0.5)
RocketEngine.status()

time.sleep(1)
print("Zwalniam...")
for engine in acceleration_engines:
    engine.stop()
    engine.__del__()

time.sleep(0.5)
RocketEngine.status()

time.sleep(1)
print("Zatrzymuje się...")
for engine in start_engines:
    engine.stop()
    engine.__del__()

time.sleep(0.5)
RocketEngine.status()