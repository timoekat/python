rate = input("Оцените работу оператора от 1 до 5: ")
rate_as_number = int(rate)


if (rate_as_number < 1):
    rate_as_number = 1

if (rate_as_number > 5):
    rate_as_number = 5

print(rate_as_number)

feedback = ""

if rate_as_number == 1:
    
    feedback = input("Расскажите, что нам улучшить: ")
elif rate_as_number == 2:
        feedback = input("расскажите, что вас смутило: ")
elif rate_as_number == 3:
        feedback = input("расскажите, как нам стать лучше")
elif rate_as_number == 4:
        feedback = input("расскажите, почему не 5")  
else:
        feedback = input("расскажите, за что похвалить оператора")    
        

print(feedback)
