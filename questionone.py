#question one 
# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"

    def power_on(self):
        return f"{self.model} is powering on..."
    
    def power_off(self):
        return f"{self.model} is powering off..."

# Inherited class: SmartphoneWithCamera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, camera_resolution):
        super().__init__(brand, model, price)
        self.camera_resolution = camera_resolution
    
    def display_info(self):
        return f"{super().display_info()}, Camera Resolution: {self.camera_resolution}MP"

    def take_picture(self):
        return f"Taking a picture with {self.camera_resolution}MP camera..."

# Creating objects for each class
basic_phone = Smartphone("Nokia", "3310", 50)
camera_phone = SmartphoneWithCamera("Apple", "iPhone 13", 999, 12)

# Displaying information
print(basic_phone.display_info())
print(basic_phone.power_on())
print(basic_phone.power_off())

print(camera_phone.display_info())
print(camera_phone.take_picture())
