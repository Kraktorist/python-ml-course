def main():
    """
    Run salary counting
    Expecting car numbers in the following format
    'a999aa', 'z345sd' etc 
    """
    print(calculate_salary())

def calculate_salary():
    """
    Count salary per day
    """
    sum_of_fines = 0
    car_number, speed = read_data()
    while not chef_detected(car_number):
        if speed_detection(speed):
            sum_of_fines += fine_defining(car_number)
        car_number, speed = read_data()
    return sum_of_fines


def chef_detected(car_number: str, chef_number: str = 'a999aa') -> bool:
    """
    Checking if it's boss car
    """
    return car_number == chef_number
    
def read_data() -> list:
    """
    Reading input
    """
    car_number = None
    speed = None
    while car_number is None or speed is None:
        try:
            car_number, speed = (input('Read car_number and speed: ')).split(' ')
            speed = float(speed)
        except:
            print("Wrong data format. Please repeat.")
    return [car_number, speed]

def speed_detection(speed: float) -> bool:
    return speed > 60 

def fine_defining(car_number: str) -> int:
    if lucky_number(car_number):
        return 1000
    if pretty_number(car_number):
        return 500
    return 100

def lucky_number(car_number: str) -> str:
    """
    Lucky number when all the digits are the same
    """
    return car_number[1] == car_number[2] == car_number[3]

def pretty_number(car_number: str) -> str:
    """
    Pretty number when two of the digits are the same
    """
    return car_number[1] == car_number[2] or car_number[1] == car_number[3] or car_number[2] == car_number[3]

if __name__ == "__main__":
    main()