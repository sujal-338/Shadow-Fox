class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print("Calling", number)

    def receive_call(self, number):
        print("Receiving call from", number)

    def take_a_picture(self):
        print("Picture taken with", self.rear_camera, "rear camera")


class Apple(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, model):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def face_id_unlock(self):
        print(self.model, "unlocked using Face ID")


class Samsung(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, model):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def samsung_pay(self):
        print(self.model, "payment done using Samsung Pay")


iphone_12 = Apple("Touch Screen", "5G", False, "12MP", "12MP", "4GB", "64GB", "iPhone 12")
iphone_13 = Apple("Touch Screen", "5G", False, "12MP", "16MP", "4GB", "128GB", "iPhone 13")

galaxy_s21 = Samsung("Touch Screen", "5G", True, "10MP", "64MP", "8GB", "128GB", "Galaxy S21")
galaxy_a52 = Samsung("Touch Screen", "4G", True, "8MP", "48MP", "4GB", "64GB", "Galaxy A52")

iphone_12.make_call("1234567890")
iphone_12.face_id_unlock()
galaxy_s21.take_a_picture()
galaxy_s21.samsung_pay()
