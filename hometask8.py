import requests
from datetime import date, datetime


class hillel_task:
    user = "aburov"
    today = date.today()
    time = datetime.now()

    current_date = today.strftime("%d/%m/%Y")
    current_time = time.strftime("%H:%M:%S")


def quantity_of_paragraphs():
    retry = 0
    word = "Pancetta"
    general_arr = []
    word_arr = []

    user_input_number = int(input("Input quantity of paragraphs: "))

    while retry < user_input_number:
        req = requests.get('https://baconipsum.com/api?type=meat-and-filler').text
        general_arr.append(req)
        retry = retry + 1

    for elem in general_arr:
        if word in elem:
            word_arr.append(elem)
        print(elem)

    with open('output.txt', 'w') as file:
        file.write(
            hillel_task.user + ", executed time: " + hillel_task.current_date + " " + hillel_task.current_time + "\n")
        file.write("Quantity of paragraphs with \'Pancetta\' word: " + str(len(word_arr)) + "\n\n")
        for item in general_arr[::-1]:
            file.write("%s\n" % item)


quantity_of_paragraphs()
