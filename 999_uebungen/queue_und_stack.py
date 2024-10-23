'''
Stack (Stapel)
Ein Stack funktioniert nach dem LIFO-Prinzip (Last-In-First-Out)
1
. Das bedeutet:
Neue Elemente werden oben auf den Stapel gelegt ("push")
Elemente werden immer vom oberen Ende des Stapels entfernt ("pop")
Das zuletzt hinzugefügte Element wird als erstes wieder
 
Queue (Warteschlange)
Eine Queue folgt dem FIFO-Prinzip (First-In-First-Out)
1
. Hierbei gilt:
Neue Elemente werden am Ende der Warteschlange eingefügt ("enqueue")
Elemente werden vom Anfang der Warteschlange entfernt ("dequeue")
Das am längsten wartende Element wird zuerst entfernt entfernt
'''

class Queue():

    def __init__(self):
        self.queue = []


    def enqueue(self, item):
        self.queue.append(item)


    def dequeue(self):
        return self.queue.pop(0)


def main():
    test = Queue()
    test.enqueue("First")
    test.enqueue("Second")
    print(test.queue)
    test.dequeue()
    print(test.queue)

if __name__ == "__main__":
    main()
