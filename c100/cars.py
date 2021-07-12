class Cars:
    def __init__(self, speed, model, colour, company):
        self.speed = speed
        self.model = model
        self.company = company
        self.colour = colour
        self.status = ''
    def show(self):
        print("Model: ", self.model)
        print("Speed: ", self.speed)
        print("Company: ", self.company)
        print("Colour: ", self.colour)
    def start(self):
        self.status = 'started'
        print(self.status)
    def stop(self):
        self.status = 'stopped'
        print(self.status)
    def changeGear(self, gear):
        self.status = 'travelling at '+ gear
        print(self.status)

bentley = Cars(100, '1927 continental', 'black', 'bentley')
bentley.show()
bentley.start()
bentley.changeGear('2nd gear')
bentley.stop()