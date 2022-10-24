import requests
from requests.exceptions import ConnectionError
from threading import Thread
from time import sleep

# функция получения информации о посте по id
def get_post(id):
    # список зеркал
    api_addr = ['https://jsonplaceholder.typicode.com', 'http://188.127.251.4:8240',]
    # получение данных, порядок последовательный из каждого адреса, пока не заблокирован
    for url in api_addr:
        result = requests.get(f'{url}/posts/{id}')
        # проверка на блокировку, если заблокировано переходим к следующему адресу
        # мне не удалось вызвать блокировку, поэтому я использовал проверку с помощью исключения ConnectionError
        # поэтому возможна и другая проверка, например по статусу ответа сервера или телу запроса
        try:
            #выводим информацию об ответе в консоль, чтобы проверить, что функция работает, при запуске в разных потоках
            print(result.content)
            return result.content
        except ConnectionError:
            continue
    # если заблокированы все адреса выводим информацию об этом
    else:
        return "Превышенение количества запросов для всех адресов"

#Пример использования,
if __name__ == '__main__':
    #просто вызываем функию, и выводим результат ее работы в консоль
    result = get_post(10)
    print(result)
    #создаем для каждоого id отдельный поток
    for id in range(1,1000):
        th1 = Thread(target=get_post, args=(1,))
        th1.start()
        th1.join()
        #
        # th2 = Thread(target=get_post, args=(1,))
        # th3 = Thread(target=get_post, args=(1,))
        # th4 = Thread(target=get_post, args=(1,))
        # th2.start()
        # th3.start()
        # th4.start()
        #
        # th1.join()
        # th2.join()
        # th3.join()
        # th4.join()



