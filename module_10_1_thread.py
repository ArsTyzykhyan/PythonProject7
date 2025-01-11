from time import sleep, time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

print("Работа функций:", time() - start_time)

threads = []
args = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]

start_time = time()
for arg in args:
    t = Thread(target=write_words, args=arg)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Работа потоков:", time() - start_time)