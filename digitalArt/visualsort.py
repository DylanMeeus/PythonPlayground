
# use sorting algorithms to hopefully create something nice..
import pygame
from random import randint
from numba import jit

@jit
def bubble_sort_step(numbers: [int]) -> '[int]':
    """ one step in the sorting algorithm, returns a slightly more ordened list """
    numbers = [num for num in numbers]
    for i in range(len(numbers)-1):
        if numbers[i+1] < numbers[i]:
            a = numbers[i+1]
            b = numbers[i]
            numbers[i] = a
            numbers[i+1] = b
    return numbers


@jit
def insertion_sort_step(numbers: [int]) -> '[int]':
    sorted_numbers = []
    for i in range(len(numbers)):
        # find the location in sorted_numbers
        j = i
        while j > 0:
            if numbers[j-1] > numbers[j]:
                # swap
                a = numbers[j]
                b = numbers[j-1]
                numbers[j] = b
                numbers[j-1] = a
            j = j - 1
        sorted_numbers.append([x for x in numbers]) # copy of current numbers state
    return sorted_numbers


def insertion_sort(numbers: [int]) -> '[int]':
    return insertion_sort_step(numbers)

@jit
def sort(numbers: [int]) -> '[[int]]':
    expected_result = sorted(numbers)
    current_sequence = numbers
    results = [current_sequence]
    while expected_result not in results:
        results.append(bubble_sort_step(results[len(results)-1]))
    return results

def create_colour_map(numbers: [int]) -> '{int, (int,int,int)}':
    colour_map = {}
    min_c = 100
    max_c = 250
    for num in numbers:
        if num not in colour_map.keys():
            colour_map[num] = (randint(min_c,max_c), randint(min_c,max_c), randint(min_c,max_c))
    return colour_map


def pygame_draw(array, stepped_array: [[int]]) -> 'None':
    radius = 10
    spacing = 10
    border_size = 20
    # we can calculate width / height based on the contents of the [[int]]
    width = (spacing + radius) * len(array) + border_size 
    height = (spacing + radius) * len(stepped_array) + border_size
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    y = 0 
    colour_map = create_colour_map(array)
    for a in stepped_array:
        x = 0
        y = y + radius + spacing 
        for i in range(len(a)):
            x = x + radius + spacing 
            colour = colour_map[a[i]] 
            pygame.draw.circle(screen, colour, (x,y), radius)
    pygame.display.update()
    pygame.image.save(screen, "pygame.png")

if __name__ == '__main__':
    print("calculating..")
    array = [randint(0,10) for x in range(0,60)] 
    stepped_array = insertion_sort(array)
    print("done sorting, time to draw!")
    pygame_draw(array, stepped_array)
    print("done, waiting for exit")
    while True:
        # wait for exit
        pass


