from datetime import datetime

employers = ['Alex', 'George', 'Ella', 'Mike']
salary = [35000, 80000, 56000, 26000]


def log_file(root):
    def logger(func):
        def wrapper(*args, **kwargs):
            logger_data = (f'{func.__name__} called on {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}'
                           f' in:{*args, *kwargs}')
            result = func(*args, **kwargs)
            with open(root, 'a', encoding='utf8') as f:
                f.write(f"{logger_data} out:{result}\n")
            return result

        return wrapper

    return logger


my_logger = log_file('log_file.txt')


@my_logger
def salary_after_nds(money, nds=13):
    time.sleep(1)
    res = []
    for i in money:
        result = i - (i / 100 * nds)
        res.append(round(result))
    return res


@my_logger
def code_name(names):
    new_name = []
    for i in names:
        new_name.append(i[::-1].title())
    return new_name


def some_magic(func1, func2):
    your_are_businessman = dict(zip(func1, func2))
    return your_are_businessman


some_magic(code_name(employers), salary_after_nds(salary))
