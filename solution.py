import math
import os
import random
from pyfiglet import Figlet
import info
import time

class Sol():
    
    def create_people():
        people_count = random.randint(0, 101)
        
        return people_count

    def explain_problem(number_of_people):
        os.system('cls||clear')
        f = Figlet(font='slant')
        ascii_banner = f.renderText('The Josephus')
        print(ascii_banner)
        print(f"Dusman askerler tarafidan kapana kisilan {number_of_people} askerin basisin.\n{number_of_people} askerinin serefli sekilde ölmesi için bir strateji belirlemen gerekiyor.\nBelirledigin stratejide her asker olusturdugunuz cemberin solundaki kisiyi olduruyor ve sira diger kisiye geciyor.\nBu işlem tek bir kişi kalana kadar devam ediyor. Yaptigin düzende hayatta kalan, yani sona kalan kişi sen olmalisin böylece askerlerin görmeden teslim olabilirsin.\nPeki kacinci sirada olursan hayatta kalirsin? ")
        return Sol.menu(number_of_people)

    def content():
        f = Figlet(font='slant')
        ascii_banner = f.renderText('The Josephus')
        print(ascii_banner)
        print("Ornek cozum yardimini gormek icin 1, soruyu tekrar gormek için 2, cevap vermek icin 3 yazın")

    def menu(number):
        Sol.content()
        choice = int(input("Cevabiniz: "))
        return Sol.call_func(choice, number)

    def call_func(number,number_of_people):
        if number == 1:
            info.call_gif()
            os.system('cls||clear')
            return Sol.menu(number_of_people)
        elif number == 2:
            os.system('cls||clear')
            return Sol.explain_problem(number_of_people)
        elif number == 3:
            entry = int(input("Cevabinizi giriniz: "))
            result = Sol.find_solution(number_of_people)
            if entry == result:
                print(f"{entry} cevabiniz dogru!")
            else:
                print("Cevabiniz yanlis. Tekrar deneyin")
                time.sleep(3)
                os.system('cls||clear')
                return Sol.explain_problem(number_of_people)
        else:
            print("Girdiginiz deger yanlis bir degerdir lütfen tekrar giriniz")
            time.sleep(3)
            os.system('cls||clear')
            return Sol.menu(number_of_people)


    def find_solution(people_count):
        for i in range(0,10):
            compare_value = math.pow(2, i)
            if people_count < compare_value:
                return Sol.calculate(people_count, math.pow(2, i - 1))
            else: 
                continue
    
    def calculate(p_count, value):
        result = p_count - value
        result = 2 * result + 1
        return result