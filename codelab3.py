#First function
#Second function
def get_average(num_list):
    total = 0
    for num in num_list:
        total += num
    return (total/len(num_list)).__round__()
#Third function
#Main function
def main():
    my_words = ['Hello', 'apple', 'one']
    my_numbers = [5,6,7,9]
    my_cards = ['2 of Hearts', '6 of Spades', 'Jack of Diamonds', 'Queen of clubs', 'King of Clubs']

    #frame_this(my_words)
    print(get_average(my_numbers))
    #print(draw_three(my_cards))

if __name__ == '__main__':
    main()