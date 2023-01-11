import view
import logger
import model


def change():
    employee = view.employee_to_s()  # находим нужную запись
    base = logger.get_base()
    result = model.search_contact(base, employee)
    view.show_found(result)  
    if 'не найдены' not in result[0] and len(base.split('\n')) > 1: # если сотрудникв несколько, уточняем поименно
        result = model.search_contact(base, view.clarification())[0]
        new_employee = view.new_employee()  
        upd = model.edit_employee(base, result, new_employee)# меняем значение в массиве на новое
        logger.update_base(upd)  # перезаписываем базу
    elif 'не найден' not in result[0]:
        result = base.split('\n')[0]
        new_employee = view.new_employee()
        upd = model.edit_employee(base, result, new_employee)
        logger.update_base(upd)

def run_base():
    while True:
        mode = view.choose_mode()
        if mode == '1':
            employee = view.new_employee()
            base = logger.get_base()
            id = model.create_id(base)
            logger.add_new(employee, id)
        elif mode == '2':
            employee = view.employee_to_s()
            base = logger.get_base()
            result = model.search_contact(base, employee)
            view.show_found(result)
        elif mode == '3':  # редактирование
            change()
        elif mode == '4':
            employee = view.employee_to_s()  # находим нужный контакт
            base = logger.get_base()
            result = model.search_contact(base, employee)
            view.show_found(result)
            if 'не найден' not in result[0] and len(base.split('\n')) > 1: # если контактов несколько, уточнить
                result = model.search_contact(base, view.clarification())[0]
                upd = model.delete_employee(base, result) # удаляем значение в массиве
                logger.update_base(upd) # перезапиываем базу
            elif 'не найден' not in result[0]: # если контакт один
                result = base.split('\n')[0]
                upd = model.delete_employee(base, result)
                logger.update_base(upd)
        else:
            view.error()
