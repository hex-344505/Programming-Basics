class WiredPhone:
    def __init__(self, color, model, inventory_number, appointment):
        self.color = color
        self.model = model
        self.inventory_number = inventory_number
        self.appointment = appointment

    def __str__(self):
        return "color: %s, model: %s, inventory_number: %i, appointment: %s" % (self.color, self.model, self.inventory_number, self.appointment)

phone = WiredPhone('Color: red','Model: A76','Inventory number: 12','Appointment: accounts department')

