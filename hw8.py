def guess_number():
    low = 1
    high = 100
    attempts = []

    print("Загадай число от 1 до 100. Я попробую угадать его!")

    while True:
        guess = (low + high) // 2
        attempts.append(guess)
        answer = input(f"Твое число {guess}? (да / больше / меньше): ").strip().lower()

        if answer == "да":
            print("Ура! Я угадала!")
            with open("results.txt", "w") as file:
                file.write(f"Загаданное число: {guess}\n")
                file.write(f"Попытки: {attempts}\n")
                file.write(f"Количество попыток: {len(attempts)}\n")
            break
        elif answer == "больше":
            low = guess + 1
        elif answer == "меньше":
            high = guess - 1
        else:
            print("Ответ должен быть: да / больше / меньше. Попробуй снова.")

guess_number()
