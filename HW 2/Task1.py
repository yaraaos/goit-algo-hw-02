import queue
import time
import random

def generate_request(req_queue, request_id):
    # Створення заявки як рядка з унікальним номером
    request = f"Request-{request_id}"
    req_queue.put(request)
    print(f"Generated and added to queue: {request}")

def process_request(req_queue):
    if not req_queue.empty():
        # Видалення заявки з черги
        request = req_queue.get()
        print(f"Processing: {request}")
    else:
        print("The queue is empty, no requests to process.")

def main():
    # Створення черги заявок
    req_queue = queue.Queue()
    # Ідентифікатор для створення унікальних заявок
    request_id = 0

    try:
        while True:
            # Генерування нових заявок
            generate_request(req_queue, request_id)
            request_id += 1
            
            # Імітація затримки перед обробкою заявки
            time.sleep(random.uniform(0.1, 0.5))
            
            # Обробка заявки
            process_request(req_queue)
            
            # Імітація затримки для наступної ітерації
            time.sleep(random.uniform(0.1, 0.5))
    except KeyboardInterrupt:
        print("\nProgram has been stopped manually.")

if __name__ == "__main__":
    main()
