from random import choice
from string import ascii_lowercase as letters


class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with that email address"

    def del_val(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            del bucket[index]
            return f"Record {key} found and deleted "
        else:
            return "No record found with that email address"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = AlgoHashTable(256)
with open("data.txt") as f:
    for line in f:
        key, value = line.split(":")
        hash_table.set_val(key, value)

print(hash_table.get_val('mashrur@example.com'))
print(hash_table.get_val('evgeny@example.com'))
print(hash_table.del_val('evgeny@example.com'))
print(hash_table.get_val('evgeny@example.com'))


list_of_domains = ['yaexample.com','goexample.com','example.com']

quotes = [  'Luck is what happens when preparation meets opportunity',
            'All cruelty springs from weakness',
            'Begin at once to live, and count each separate day as a separate life',
            'Throw me to the wolves and I will return leading the pack']


def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))


def get_domain(list_of_domains):
    return choice(list_of_domains)


def get_quotes(list_of_quotes):
    return choice(list_of_quotes)


def generate_records(length_of_name, list_of_domains, total_records, list_of_quotes):
    with open("data.txt", "w") as to_write:
        for num in range(total_records):
            key = generate_name(length_of_name)+"@"+get_domain(list_of_domains)
            value = get_quotes(quotes)
            to_write.write(key + ":" + value + "\n")
        to_write.write("mashrur@example.com:Don't let me leave Murph\n")
        to_write.write("evgeny@example.com:All I do is win win win no matter what!\n")


generate_records(10, list_of_domains, 100000, quotes)
