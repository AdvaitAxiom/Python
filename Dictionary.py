marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

print(marks, type(marks))
print(marks["Alice"])  #accessing value using key
marks["Eve"] = 88  #adding a new key-value pair
print(marks, type(marks))

#unorderd, mutable, indexed, can have duplicate values but not duplicate keys
#dictionary within a dictionary
students = {
    "Alice": {
        "age": 20,
        "grade": "A"
    },
    "Bob": {
        "age": 22,
        "grade": "B"
    }
}
print(students)

#methods
print(marks.keys())  #returns a view object of keys
print(marks.values())  #returns a view object of values
print(marks.items())  #returns a view object of key-value pairs
print("Alice" in marks)  #returns True if "Alice" is a key in marks, False otherwise
marks.pop("Charlie")  #removes the key "Charlie" and its associated value
print(marks)    
# marks.clear()  #removes all key-value pairs from the dictionary
marks.update({"Frank": 80, "Grace": 95})  #adds multiple key-value pairs to the dictionary
print(marks)
print(marks.get("Bob"))  #returns the value associated with the key "Bob", or None if the key is not found
print(marks.get("Charlie", "Not Found"))  #returns "Not Found" since "Charlie" is not a key in marks
 
