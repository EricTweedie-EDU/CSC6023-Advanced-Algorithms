# Eric Tweedie Module 5 Program Assignment
# implement a Double Array Queue and test is for a very large case (100,000 randomly decided operations of enqueue and dequeue)
# Program should keep track of the number of costly operations and cheap operations and print them after running
# At the beginning of its run, program should also ask the user for the ratio between enqueue and dequeue operations
import random

# Function to perform enqueue and dequeue operations
class Queue:
    def __init__(self):
        self.a_in = []
        self.a_out = []
        self.costly = 0
        self.cheap = 0

    def enqueue(self, x):
        self.a_in.append(x)
        self.cheap += 1

    def dequeue(self):
        if (self.a_out == [] and self.a_in == []):
            self.cheap += 1
        if (self.a_out == [] and self.a_in != []):
            for x in self.a_in:
                self.a_out.append(x)
            self.a_in = []
            self.costly += 1
        try:
            return self.a_out.pop(0)
        except IndexError:
            "dequeue is empty"
        
        if self.out != []:
            self.cheap += 1
        
        

        
def main():
    queue = Queue()
    while True:
        eq_ratio = int(input("Enter the percentage of enqueue operations between 33 and 67: "))
        if eq_ratio <= 32 or eq_ratio >= 68:
            print("Invalid enqueue percentage. Please enter a value between 67 and 33.")
        else:
            break
    
    deq_ratio = 100 - eq_ratio
    print(f"Enqueue percentage is {eq_ratio} % and dequeue percentage is {deq_ratio} %\n")
    # Perform enqueue and dequeue operations randomly
    for _ in range(100000):
        if random.randrange(100) < eq_ratio:
            queue.enqueue(random.randint(0, 100000))
        else:
            queue.dequeue()
    
    print(f"Total cheap operations: {queue.cheap}, with total percentage {100*queue.cheap/(queue.costly+queue.cheap):.4f} %")
    print(f"Total costly operations: {queue.costly}, with total percentage {100*queue.costly/(queue.costly+queue.cheap):.4f} %")
    
main()