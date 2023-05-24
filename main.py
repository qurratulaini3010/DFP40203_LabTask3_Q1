import os
laptop = {"name": "Laptop Asus F15 Gaming",
     "description": "Armed for combat, the TUF Gaming F15 features up to a 10th Gen Intel® Core™ i7 CPU with "
                    "6 cores and 12 threads to tear through serious gaming, streaming, and heavy duty "
                    "multitasking.",
     "specifications": {
         "spec1": "10TH GEN INTEL®CORE™ I7 CPU",
         "spec2": "NVIDIA® GEFORCE®GTX 1660 TI GPU",
         "spec3": "1TB SSD NVME PCIE"
     }

     }

# Define the filename for the reviews file
reviews_filename = "laptop_reviews.txt"


# Function to display the product information


def display_baju_info():
    """Displays the product description and specifications."""
    print("laptop Name:", laptop['name'])
    print("laptop Description:", laptop['description'])
    print("laptop Specifications:")
    for spec in laptop['specifications']:
        print("-", laptop['specifications'][spec])


# Function to display the previous reviews
def display_previous_reviews():
    if os.path.isfile(reviews_filename):
        with open(reviews_filename, "r") as review_file:
            reviews = review_file.read()
            print("Previous Reviews:\n" + reviews)
    else:
        print("No previous reviews found.")


# Function to prompt the user for their review
def prompt_for_review():
    criteria1 = input("Please rate the intel (1-5): ")
    criteria2 = input("Please rate the Graphics Card (1-5): ")
    criteria3 = input("Please rate the Hard disk (1-5): ")

    # Validate user input
    if criteria1.isdigit() and criteria2.isdigit() and criteria3.isdigit():
        review = "Intel: " + criteria1 + ", Graphics Card: " + criteria2 + ", Hard disk: " + criteria3 + "\n"
        return review
    else:
        print("Invalid input. Please enter a number from 1 to 5.")
        return None


# Main program loop
while True:
    print("\nWelcome to the product review program!")
    display_baju_info()

    user_choice = input("1.write a review\n2.view previous reviews\n3. quit\nPlease enter the following number to "
                        "choose: ")

    if user_choice == "1":
        review = prompt_for_review()
        if review:
            with open(reviews_filename, "a") as reviews_file:
                reviews_file.write(review)
                print("Thank you for your review!")

    elif user_choice == "2":
        display_previous_reviews()

    elif user_choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")
