
# use sorting algorithms to hopefully create something nice..
import pygame
from random import randint
from numba import jit

################# MERGE SORT #############################

@jit
def merge_sort_step(numbers: [int], intermediate_values: [int] = []) -> '([int], [int])':
    # split numbers into sublists, compare and merge these
    if len(numbers) <= 1:
        return (numbers, intermediate_values)
    left = []
    right = []
    for i in range(len(numbers)):
        if i < len(numbers) // 2:
            left.append(numbers[i])
        else:
            right.append(numbers[i])
    left = merge_sort_step(left, intermediate_values)[0]
    right = merge_sort_step(right, intermediate_values)[0]
    merged = merge(left, right)
    intermediate_values.append(merged)
    return (merged, intermediate_values)

# we don't need to manually do the merge here, we care about the result not the intermediate values
def merge(left: [int], right: [int]) -> '[int]':
    if left != None and right != None:
        left.extend(right)
        return sorted(left)
    else:
        return sorted(left) if right == None else sorted(right)


def merge_sort(numbers: [int]):
    return merge_sort_step(numbers)[1]




################ END MERGE SORT ###########################
################# BUBBLE SORT #############################
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
def bubble_sort(numbers: [int]) -> '[[int]]':
    expected_result = sorted(numbers)
    current_sequence = numbers
    results = [current_sequence]
    while expected_result not in results:
        results.append(bubble_sort_step(results[len(results)-1]))
    return results

################# END BUBBLE SORT ##########################
################## INSERTION SORT ##########################

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

################# END INSERTION SORT #########################
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
    stepped_array = merge_sort(array)
    print("done sorting, time to draw!")
    pygame_draw(array, stepped_array)
    print("done, waiting for exit")
    while True:
        # wait for exit
        pass


