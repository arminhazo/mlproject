# mlproject/lib.py
from mlproject.distance import haversine

def try_me():
    distance = haversine(1, 2, 3, 4)
    print(f'The distance between 1,2 and 3,4 is: {distance}')
    return distance


if __name__ == "__main__":
    try_me()
