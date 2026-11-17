from data_access import DbFunctions
class Service:
    def __init__(self):
        self.service = DbFunctions()
        
        
    def validate_new_acc(self,card_name,goal_balance=None):
        if len(card_name.strip()) == 0:
            raise ValueError('Ошибка! Пустое поле названия счёта.')
        elif goal_balance is not None and goal_balance <= 0:
            raise ValueError('Ошибка! Некорректно введена цель.')
        else:
            self.service.create_new_account(card_name,goal_balance)
            
            
    def validate_add_balance(self,account_id,amount,description = None):
        if amount <= 0:
            raise ValueError('Ошибка! Сумма меньше или равна нулю.')
        data = self.service.get_accounts()
        account_found = False
        for i in data:
            if i['id'] == account_id:
                account_found = True
                break
        if not account_found:
            raise ValueError("Аккаунта с таким id не существует.")
        else:
            self.service.add_balance(account_id,amount,description = description)
            
            
    def validate_out_balance(self,account_id,amount,description = None):
        if amount <= 0:
            raise ValueError('Ошибка! Сумма меньше или равна нулю!')
        data = self.service.get_accounts()
        account_found = False
        for i in data:
            if i['id'] == account_id:
                account_found = True
                if amount > i['balance']:
                    raise ValueError("Недопустимая сумма съёма денег.")
                break
        if not account_found:
            raise ValueError("Аккаунт с таким id не существует!")
        else:
            self.service.out_balance(account_id,amount,description = description)
            
            
    def validate_transfer_balance(self,from_account_id,receiver_account_id,amount,description = None):
        if from_account_id == receiver_account_id:
            raise ValueError("Нельзя перевести деньги самому себе!")
        if amount <= 0:
            raise ValueError('Недопустимая сумма перевода денег.')
        data = self.service.get_accounts()
        from_found = False
        receiver_found = False
        for i in data:
            if i['id'] == from_account_id:
                from_found = True
                if i['balance'] < amount:
                    raise ValueError('Недостаточно средств!')
            elif i['id'] == receiver_account_id:
                receiver_found = True
        if from_found and receiver_found:
            self.service.transfer_balance(from_account_id,receiver_account_id,amount,description = description)
        else:
            raise ValueError('Неверно введены данные получателя или отправителя.')
    def validate_get_accounts(self):
        data = self.service.get_accounts()
        data_list = []
        for i in data:
            string = f'ID: {i['id']} Название счёта: {i['card_name']} Баланс: {i['balance']} Цель: {i['goal_balance']}'
            data_list.append(string)
        return data_list
    
    
    def validate_get_transactions(self):
        data = self.service.get_transactions()
        data_list = []
        for i in data:
            string = f'Имя счёта: {i['card_name']}, Тип перевода: {i['transaction_type']}, Сумма: {i['amount']}, Описание: {i['description']}, Дата и время: {i['date_time']}'
            data_list.append(string)
        return data_list