import time
import random
from colorama import init, Fore, Style
import os
import sys
import webbrowser
print(Fore.GREEN + "Welcome to Math Practice!" + Style.RESET_ALL)
time.sleep(1)
os.system('clear')

def get_user_input():
  while True:
    # Ask the user for the type of numbers
    number_type = input("Enter the type of numbers you want to practice with. Whole numbers (w), decimals (d), or exit (e): ")
    if number_type not in ["w", "d", "e"]:
      print(Fore.RED + "Error: Invalid number type. Please try again." + Style.RESET_ALL)
      continue
    elif number_type == "e":
      exit()
    elif number_type == "d":
      good_input = False
      while not good_input:
        try:
          decimal_places = int(input("Enter the number of decimal places: "))
          good_input = True
        except ValueError:
          print(Fore.RED + "Error: Invalid number of decimal places. Please enter a number." + Style.RESET_ALL)
          continue
    else:
      decimal_places = 0  
    
    # Ask the user for the range of numbers
    while True:
      try:
        min_range = int(input("Enter the minimum value in the range: "))
        max_range = int(input("Enter the maximum value in the range: "))
      except ValueError:
        print(Fore.RED + "Error: Invalid range. Please enter a number." + Style.RESET_ALL)
      
        continue
      
      # Make sure the minimum range is less than the maximum range
      if min_range >= max_range:
        print(Fore.RED + "Error: Invalid range. The minimum value must be less than the maximum value." + Style.RESET_ALL)
        continue
      
      break
    
    # Ask the user for the math operations
      
    while True:
      try:
        operations = input("Enter the math operations (+, -, *) you want to practice with: ")
        good_input = True
      except ValueError:
        print(Fore.RED + "Error: Invalid math operations. Please enter a number." + Style.RESET_ALL)
        continue
        
      # Make sure the operations are valid
      if operations not in ["+", "-", "*"]:
        print(Fore.RED + "Error: Invalid math operations. Please enter a number." + Style.RESET_ALL)
        continue
        
      break
      
    
    # Ask the user for the number of test questions
    while True:
      try:
        num_questions = int(input("Enter the number of test questions you want to answer: "))
      except ValueError:
        print(Fore.RED + "Error: Invalid number of test questions. Please enter a number." + Style.RESET_ALL)
        continue
      break
    
    return number_type, min_range, max_range, operations, num_questions, decimal_places

def generate_test_questions(number_type, min_range, max_range, operations, num_questions, decimal_places):
  # Generate the test questions
  test_questions = []
  for i in range(num_questions):
    if number_type == "w":
      num1 = random.randint(min_range, max_range)
      num2 = random.randint(min_range, max_range)
    else:
      num1 = round(random.uniform(min_range, max_range), decimal_places)
      num2 = round(random.uniform(min_range, max_range), decimal_places)
  
      
    operation = random.choice(operations)
    question = f"{num1} {operation} {num2}"
    test_questions.append(question)
  return test_questions

def ask_questions(test_questions, decimal_places):
  # Keep track of the number of correct answers
  num_correct = 0
  
  # Start the timer
  start_time = time.time()
  
  # Ask the questions
  for question in test_questions:
    valid_answer = False
    while not valid_answer:
      answer = input(f"{question} = ")
      
      # Check if the answer is a valid number
      try:
        float(answer)
        valid_answer = True
      except ValueError:
        print(Fore.RED + "Error: Invalid answer. Please enter a number." + Style.RESET_ALL)

    rounded_computer_answer = round(eval(question), decimal_places) 
    rounded_user_answer = round(float(answer), decimal_places)
    if rounded_computer_answer == rounded_user_answer:
      num_correct += 1
      print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
      print("")
    else:
      print(Fore.RED + "Incorrect!" + Style.RESET_ALL)
      print(Fore.RED + "The correct answer was " + str(eval(question)) + "." + Style.RESET_ALL)
      print("")
  
  # Stop the timer
  end_time = time.time()
  
  return num_correct, end_time - start_time

def main():
  
  # Get the user input
  number_type, min_range, max_range, operations, num_questions, decimal_places = get_user_input()

  
  # Generate the test questions
  test_questions = generate_test_questions(number_type, min_range, max_range, operations, num_questions, decimal_places)
  
  # Ask the questions
  num_correct, elapsed_time = ask_questions(test_questions, decimal_places)
  
  # Calculate the accuracy
  accuracy = num_correct / num_questions * 100
  if accuracy <= 50:
    print(Fore.RED + "Try harder next time! Here is your reward." + Style.RESET_ALL)
    time.sleep(1.1)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  elif accuracy == 100:
    print(Fore.GREEN + "Congratulations! You got a perfect score!" + Style.RESET_ALL)
  
  # Print the results
  print(f"You answered {num_correct} out of {num_questions} questions correctly.")
  print(f"Your accuracy was {accuracy:.2f}%.")
  print(f"It took you {elapsed_time:.2f} seconds to complete the test.")
  

if __name__ == "__main__":
  main()
