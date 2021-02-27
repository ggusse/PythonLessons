class Automobile:

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return ('Make: %s, Model: %s, Color: %s, Year: %d, Mileage: %d\n' %
                (self.make, self.model, self.color, self.year, self.mileage))

    def add_veh(self):
        veh = car.__str__()
        inventory.append(veh)
        print('Vehicle added')

    def remove_veh(self):
        for i in inventory:
            if i == car.__str__():
                inventory.remove(i)
                print('Vehicle removed')
            
    def update_veh(self):
        for i in inventory:
            if i == car.__str__():
                print('Vehicle found. Enter updated vehicle information.')
                info = get_car_info()
                new_info = Automobile(info[0],info[1],info[2],info[3],info[4])
                position = inventory.index(i)
                inventory.remove(i)
                veh = new_info.__str__()
                inventory.insert(position, veh)
                        

def get_car_info():
    make = str(input('Enter make of car: '))
    model = str(input('Enter model of car: '))
    color = str(input('Enter color of car: '))
    year = int(input('Enter year of car: '))
    mileage = int(input('Enter mileage of car: '))
    car_info = [make, model, color, year, mileage]
    return car_info

print('Opening inventory file...')
inventory_file = open('LotInventory.txt','r+')

inventory = inventory_file.readlines()

inventory_file.close()

print(inventory)

user_input = input('Select an action (p = print inventory file, a = add a vehicle, r = remove a vehicle, u = find a vehicle to update, s = save to file, q = quit): ')
while user_input != 'q':
    if user_input == 'p':
        inventory_file = open('LotInventory.txt','r')
        current_file = inventory_file.read()
        print(current_file)

    elif user_input == 's':
        inventory_file = open('LotInventory.txt','w+')
        for i in range(len(inventory)):
            inventory_file.write(inventory[i])
        inventory_file.close()

    else:
        info = get_car_info()
        car = Automobile(info[0],info[1],info[2],info[3],info[4])

        if user_input == 'a':
            car.add_veh()

        elif user_input == 'r':
            car.remove_veh()

        elif user_input == 'u':
            car.update_veh()

        else:
            print('Invalid selection')

    user_input =  input('Select an action (p = print inventory file, a = add a vehicle, r = remove a vehicle, u = find a vehicle to update, s = save to file, q = quit): ')
