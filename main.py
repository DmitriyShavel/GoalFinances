from services import Service
main = Service()
while True:
    print("1.Создать счёт\n2.Пополнить счёт\n3.Записать расход\n4.Перевести деньги между счетами\n5.Показать сводку по счетам\n6.Последние операции\n7.Выйти из программы")
    choice = input("Выберите опцию:")
    match choice:
        case '1':
            card_name = input("Введите название вашего счёта:")
            goal_balance = input("Введите вашу целевую сумму (оставьте поле пустым если цель не нужна.):").strip()
            if len(goal_balance) == 0:
                try:
                    main.validate_new_acc(card_name)
                except Exception as error:
                    print(error)
                    continue
            else:
                try:
                    goal_balance = int(goal_balance)
                except ValueError:
                    print("Похоже, вы ввели буквы")
                    continue
                try:
                    main.validate_new_acc(card_name,goal_balance)
                except Exception as error:
                    print(error)
                    continue
        case '2':
            try:
                account_id = int(input("Введите id счёта который вы хотите пополнить:"))
            except ValueError:
                print("Вы ввели буквы.")
                continue
            try:
                amount = int(input("Введите сумму которую на которую вы хотите пополнить счёт:"))
            except ValueError:
                print("Вы ввели буквы.")
                continue
            description = input("Введите комментарий (оставьте поле пустым если комментарий не нужен.):").strip()
            if len(description) == 0:
                description = None
                try:
                    main.validate_add_balance(account_id,amount)
                except Exception as error:
                    print(error)
                    continue
            else:
                try:
                    main.validate_add_balance(account_id,amount,description)
                except Exception as error:
                    print(error)
                    continue
        case '3':
            try:
                account_id = int(input("Введите id счёта с которого вы хотите снять сумму: "))
            except ValueError:
                print("Вы ввели буквы!")
                continue
            try:
                amount = int(input('Введите сумму которую вы хотите снять:'))
            except ValueError:
                print("Вы ввели буквы!")
                continue
            description = input('Введите комментарий или оставьте поле пустым:').strip()
            if len(description) == 0:
                description = None
                try:
                    main.validate_out_balance(account_id,amount)
                except Exception as error:
                    print(error)
            else:
                try:
                    main.validate_out_balance(account_id,amount,description)
                except Exception as error:
                    print(error)
                    continue
        case '4':
            try:
                from_id = int(input('Введите id с какого счёта вы хотите прислать деньги:'))
            except ValueError:
                print("Вы ввели буквы.")
                continue
            try:
                receiver_id = int(input("Введите id получателя:"))
            except ValueError:
                print("Вы ввели буквы")
                continue
            try:
                amount = int(input("Введите сумму для перевода:"))
            except ValueError:
                print("Вы ввели буквы.")
                continue
            description = input("Введите комментарий или оставьте поле пустым:").strip()
            if len(description) == 0:
                description = None
                try:
                    main.validate_transfer_balance(from_id,receiver_id,amount)
                except Exception as error:
                    print(error)
                    continue
            else:
                try:
                    main.validate_transfer_balance(from_id,receiver_id,amount,description)
                except Exception as error:
                    print(error)
                    continue
        case '5':
            data = main.validate_get_accounts()
            if not data:
                print("Список аккаунтов пока пуст...")
                continue
            for i in data:
                print(i)
        case '6':
            data = main.validate_get_transactions()
            if not data:
                print("Транзакций пока нет...")
                continue
            for i in data:
                print(i)
        case '7':
            main.service.close_connection()
            exit()