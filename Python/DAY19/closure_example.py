def outer_greeting(greeting_prefix):
    # 'greeting_prefix' is an enclosing variable
    
    def inner_greeting(name):
        # The inner function remembers 'greeting_prefix'
        return f"{greeting_prefix}, {name}!"
    
    return inner_greeting

print("===  Greeting Closure ===")
say_hello = outer_greeting("Hello")
say_namaste = outer_greeting("Namaste")


print(say_hello("Om"))       
print(say_namaste("Rahul"))