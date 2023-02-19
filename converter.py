class Converter:

    symbols = {
        (0, 0, 0): ':dark_sunglasses:',
        (255, 0, 0): ':rage:',
        (255, 255, 0): ':pensive:',
        (255, 255, 255): ':roll_of_paper:',
        (0, 255, 0): ':sick:',
        (0, 255, 255): ':snowflake:',
        (0, 0, 255): ':cold_face:',
        (175, 30, 80): ':mx_claus_tone5:',
        (90, 104, 120): ':new_moon_with_face:',
        (255, 170, 50): ':cheese:',
        (80, 0, 0): ':vampire_tone5:'

    }

    max_rows = 13
    max_cols = 13

    def __init__(self):
        pass

    # gets the symbol in the symbols dictionary that has the least
    # color difference from the provided pixel
    def get_closest_symbol(self, pixel):
        mindist = 1000000
        closest_match = None
        for sym in self.symbols.keys():
            d = self.dist(pixel, sym)
            if d < mindist:
                mindist = d
                closest_match = sym
        return closest_match

    # gets the distance between two points in 3D space
    # doesn't do the squareroot because I just need to minimize distance not get the exact value
    def dist(self, c1, c2):
        return (c1[0] - c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2

    #converts a matrix of [r,g,b] values to the string containing discord emojis
    def convert(self, pixel_matrix):
        output = ''
        for row in pixel_matrix:
            for pixel in row:
                output = output + self.symbols[self.get_closest_symbol(pixel)]
            output = output + '\n'
        return output
    