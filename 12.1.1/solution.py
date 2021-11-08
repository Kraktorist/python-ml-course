import csv
import os
import re

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if brand == '':
            raise ValueError("Brand is not defined")
        self.brand = brand
        self.carrying = float(carrying)
        self.photo_file_name = photo_file_name
        if self.get_photo_file_ext() not in [".jpg", ".jpeg", ".png", ".gif"]:
            raise ValueError("Wrong image extension")

    def get_photo_file_ext(self):
        """
        Getting image extension
        """
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):

    car_type = "car"

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):

    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            result = re.fullmatch('([0-9.]+)x([0-9.]+)x([0-9.]+)',body_whl)
            self.body_length = float(result.group(1))
            self.body_width = float(result.group(2))
            self.body_height = float(result.group(3))
        except:
            self.body_length, self.body_width, self.body_height = [0.0, 0.0, 0.0]

    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height


class SpecMachine(CarBase):

    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        if extra == '':
            raise ValueError("Extra information is not defined")
        self.extra = extra


def get_car_list(csv_filename):
    # car_type;brand;passenger_seats_count;photo_file_name;body_whl;carrying;extra
    car_list = []
    with open(csv_filename, newline='',encoding="utf8") as csv_fd:
        # reader = csv.reader(csv_fd, delimiter=';')
        # next(reader)  # пропускаем заголовок
        # for row in reader:
        #     try:
        #         if row[0] == "car":
        #             car_list.append(Car(row[1], row[3], row[5], row[2]))
        #         if row[0] == "spec_machine":
        #             car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
        #         if row[0] == "truck":
        #             car_list.append(Truck(row[1], row[3], row[5], row[4]))
        #     except:
        #         pass
        reader = csv.DictReader(csv_fd, delimiter=";")
        for row in reader:
            # print(row)
            try:
                if row["car_type"] == "car":
                    car_list.append(
                        Car(
                            row["brand"],
                            row["photo_file_name"],
                            float(row["carrying"]),
                            int(row["passenger_seats_count"])
                        )
                    )
                if row["car_type"] == "truck":
                    car_list.append(
                        Truck(
                            row["brand"],
                            row["photo_file_name"],
                            float(row["carrying"]),
                            row["body_whl"]
                        )
                    )
                if row["car_type"] == "spec_machine":
                    car_list.append(
                        SpecMachine(
                            row["brand"],
                            row["photo_file_name"],
                            float(row["carrying"]),
                            row["extra"]
                        )
                    )
            except:
                pass
    return car_list