class Power_unit:
    
    def __init__(self, power='выключено'):
        self.power = power
         
    def on_power(self):
        self.power = 'включено'
        return  f'Питание: {self.power}'
    
class Motherboard:
    
    def __init__(self, chipset):
        self.chipset = chipset
        
    def redistribute_voltage(self):
        if self.chipset == 'серия А':
            return  f'Перераспределение напряжения подходит для офиса'    
        elif self.chipset == 'серия В':
            return  f'Перераспределение напряжения подходит для игры'           
        
class CPU:

    def __init__(self, clock_frequency, number_of_cores):
        self.clock_frequency = clock_frequency
        self.number_of_cores = number_of_cores
                      
    def activate_turbo_mode(self):
        return  f'Турбо режим включен'   
        
class RAM:

    def __init__(self, memory_capacity, frequency_memory):
        self.memory_capacity = memory_capacity
        self.frequency_memory = frequency_memory
                    
    def load_data(self):
        return 'Загрузка данных началась'      
        
    def upload_data(self):
        return  'Выгружаю данные'
      
class SSD:

    def __init__(self, capacity):
        self.capacity = capacity
        
    def save_data(self):
        return  'Данные сохранены'  
        
    def delete_data(self):
        return  'Данные удалены' 
        
class Video_card:

    def __init__(self, model, memory_capacity2):
        self.model = model
        self.memory_capacity2 = memory_capacity2
              
    def display(self):
        return  'Изображение на экране'  

class Computer(Power_unit, Motherboard, CPU, RAM, SSD, Video_card):
    def __init__(self, brand, power, chipset, clock_frequency, number_of_cores, memory_capacity, frequency_memory, capacity, model, memory_capacity2):
        self.__brand = brand
        Power_unit.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CPU.__init__(self, clock_frequency, number_of_cores)
        RAM.__init__(self, memory_capacity, frequency_memory)
        SSD.__init__(self,capacity)
        Video_card.__init__(self, model, memory_capacity2)
        
    def about_comp(self):
        return f'''Бренд компьютера: {self.__brand}, 
питание: {self.power}, 
чипсет материнской платы: {self.chipset}, 
ядер: {self.number_of_cores}, 
ssd: {self.capacity}, 
видеокарта: {self.model}, 
ram: {self.memory_capacity} Гб.'''

comp = Computer('Lenovo', 'включено', 'серия А', 3.5, 8, '1 Tb', 'Nvidea', '12 Gb', 32, 3200)
print(comp.about_comp())