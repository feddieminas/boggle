#import os
from string import ascii_uppercase
from random import choice

#SCRIPT_PATH = os.path.join(os.getcwd(), os.path.dirname(__file__))

def make_grid(width,height):
    """
    Creates a grid that will hold all of the tiles for a boggle game
    """
    return {(row,col): choice(ascii_uppercase) 
        for row in range(height) 
        for col in range(width)}
        

def neighbours_of_position(coords):
    """
    Get neighbours of a given position
    """
    row = coords[0]
    col = coords[1]
    
    #Assign each of the neighbours
    # Top-left to top-right
    top_left = (row-1, col-1)
    top_center = (row-1, col)
    top_right = (row-1, col+1)
    
    #left to right
    left = (row, col-1)
    # The (row, col) coordinates passed to this
    # function are situated here
    right = (row, col+1)
    
    #Bottom-left to bottom-right
    bottom_left = (row+1, col-1)
    bottom_center = (row+1, col)
    bottom_right = (row+1, col+1)
    
    return [top_left, top_center, top_right, left, right, bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    """
    Get all of the possible neighbours for each position in
    the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours    
        
def path_to_word(grid, path):
    """
    Add all of the letters on the path to a string
    """
    return ''.join([grid[p] for p in path])

#def word_in_dictionary(word, dict):
    #return word in dict
    
def search(grid, dictionary): 
    """
    Search through the paths to locate words by matching
    strings to words in a dictionary. Better to store words as paths instead of strings because a letter can be repeated while a word not.
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary # we unpack the dict tuple into stems and full words
    
    def do_search(path):
        word = path_to_word(grid, path)
        #if word_in_dictionary(word, dictionary): #old word in dictionary
        if word in full_words: # check if we have find a real word 
            paths.append(path)
        if word not in stems: # we use the stems to see if we can ignore the rest of the path we're currently on
            return 
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    
def get_dictionary(dictionary_file):
    """
    Load Dictionary File
    """
    #if not dictionary_file.startswith('/'):
        # if not absolute, then make path relative to our location:
        #dictionary_file = os.path.join(SCRIPT_PATH, dictionary_file)    
    full_words, stems = set(), set() # full words and partial words
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
            
        return full_words, stems    
        #return {w.strip().upper() for w in f} # ex [w.strip().upper() for w in f]


def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))
    
    
def main():
    """
    This is the function that will run the whole project
    """
    grid = make_grid(4,4)
    
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    display_words(words)
    
if __name__ == "__main__": # so no probem when run initesting
    main()
    
    
    
    
    
    
    

    
    
    
    
    
        
        
            
            
            
            
            
        
        
    
    