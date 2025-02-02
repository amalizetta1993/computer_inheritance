class Computer:
    def __init__(self, brand, power_unit, mother, cpu, ssd, video, ram):
        self.__brand = brand
        self.__power_unit = power_unit
        self.__mother = mother
        self.__cpu = cpu
        self.__ssd = ssd
        self.__video = video
        self.__ram = ram      
    
    def about_comp(self):
        return f'''Бренд компьютера: {self.__brand}, 
питание: {self.__power_unit.power}, 
чипсет материнской платы: {self.__mother.chipset}, 
ядер: {self.__cpu.number_of_cores}, 
ssd: {self.__ssd.capacity}, 
видеокарта: {self.__video.model}, 
ram: {self.__ram.memory_capacity} Гб.'''
    
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

    def __init__(self, model, memory_capacity):
        self.model = model
        self.memory_capacity = memory_capacity
              
    def display(self):
        return  'Изображение на экране'  


power_unit = Power_unit()
mother = Motherboard('серия А')
cpu = CPU(3.5, 8)
ssd = SSD('1 Tb')
video = Video_card('Nvidea', '12 Gb')
ram = RAM(32, 3200)

comp = Computer('Lenovo', power_unit, mother, cpu, ssd, video, ram)
print(comp.about_comp())