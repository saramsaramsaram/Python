class TV:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    def setChannel(self, channel):
        self.channel = channel
    def show(self):
        print(f'현재 채널 : {self.channel}, 볼륨 : {self.volume}, 전원 : {self.on}')
    def OnOff(self):
        self.on = not self.on 
t = TV(7, 10, True)
t.show()
t.setChannel(10)
t.show()
t.OnOff()
t.show()
