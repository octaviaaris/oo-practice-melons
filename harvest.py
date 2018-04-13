############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color,
                 is_seedless, is_bestseller):
        """Initialize a melon type."""

        self.pairings = []

        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green',
                     True, True)
    casaba = MelonType('cas', 'Casaba', 2003, 'orange',
                       False, False)
    crenshaw = MelonType('cren', 'Crenshaw', 1996, 'green',
                         False, False)
    y_watermelon = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow',
                             False, True)

    musk.add_pairing('mint')
    casaba.add_pairing('strawberries', 'mint')
    crenshaw.add_pairing('proscuitto')
    y_watermelon.add_pairing('ice cream')

    all_melon_types.append(musk)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(y_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "\n{melon} pairs with".format(melon=melon.name)
        for pair in melon.pairings:
            print "- {pair}".format(pair=pair)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_lookup = {}

    for melon in melon_types:
        melon_type_lookup[melon.code] = melon

    return melon_type_lookup


############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a specific melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self, min_shape_rating, min_color_rating, *bad_fields):
        """Takes minimum ratings for shape and color and checks if a field
        is poisoned to categorize melons as sellable or not."""

        return self.shape_rating > min_shape_rating and \
            self.color_rating > min_color_rating and \
            self.field not in bad_fields


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_type_lookup = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melon_type_lookup["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melon_type_lookup["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melon_type_lookup["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melon_type_lookup["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melon_type_lookup["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melon_type_lookup["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melon_type_lookup["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melon_type_lookup["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melon_type_lookup["yw"], 7, 10, 3, "Sheila")

    all_melons = [melon_1, melon_2, melon_3,
                  melon_4, melon_5, melon_6,
                  melon_7, melon_8, melon_9]

    return all_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable(5, 5, 3):
            sellable = 'CAN BE SOLD'
        else:
            sellable = 'NOT SELLABLE'

        print "Harvested by {harv} from Field #{field} {sellable}".format(
            harv=melon.harvester, field=melon.field, sellable=sellable)


melons = make_melons(make_melon_types())
get_sellability_report(melons)
