ELEMENT = {}

# Data from ptable.com
ELEMENT_DATA = {
    "Er": ("Erbium", 68, 167.259),
    "Am": ("Americium", 95, 243),
    "At": ("Astatine", 85, 210),
    "Ac": ("Actinium", 89, 227),
    "Zn": ("Zinc", 30, 65.38),
    "Zr": ("Zirconium", 40, 91.224),
    "Eu": ("Europium", 63, 151.964),
    "Pa": ("Protactinium", 91, 231.03),
    "Uup": ("Ununpentium", 115, 288),
    "Ta": ("Tantalum", 73, 180.94),
    "He": ("Helium", 2, 4.002602),
    "Sb": ("Antimony", 51, 121.760),
    "I": ("Iodine", 53, 126.90),
    "Ru": ("Rutherium", 44, 101.07),
    "U": ("Uranium", 92, 238.02),
    "H": ("Hydrogen", 1, 1.008),
    "Cs": ("Caesium", 55, 132.90),
    "Au": ("Gold", 79, 196.96),
    "Ho": ("Holmium", 67, 164.93),
    "Cu": ("Copper", 29, 63.546),
    "Dy": ("Dysprosium", 66, 162.500),
    "Bh": ("Bohrium", 107, 272),
    "Md": ("Mendelevium", 101, 258),
    "Li": ("Lithium", 3, 6.94),
    "Rg": ("Roentgenium", 111, 280),
    "Hf": ("Hafnium", 72, 178.49),
    "Si": ("Silicon", 14, 28.085),
    "F": ("Fluorine", 9, 18.998),
    "Cd": ("Cadmium", 48, 112.414),
    "Sr": ("Strontium", 38, 87.62),
    "O": ("Oxygen", 8, 15.999),
    "Pm": ("Promethium", 61, 145),
    "Al": ("Aluminum", 13, 26.981),
    "S": ("Sulfur", 16, 32.06),
    "Ra": ("Radium", 88, 226),
    "Be": ("Beryllium", 4, 9.0121),
    "Ds": ("Damstaudium", 110, 281),
    "Ag": ("Silver", 47, 106.42),
    "Rb": ("Rubidium", 37, 85.4678),
    "Xe": ("Xenon", 54, 131.293),
    "Db": ("Dubnium", 105, 268),
    "Hg": ("Mercury", 80, 200.59),
    "Tm": ("Thulium", 69, 168.93),
    "Ce": ("Cerium", 58, 140.116),
    "Rh": ("Rhodium", 45, 102.90),
    "Br": ("Bromine", 35, 79.904),
    "Sm": ("Samarium", 62, 150.36),
    "Uut": ("Ununtrium", 113, 284),
    "Fl": ("Flerovium", 114, 289),
    "Pu": ("Plutonium", 94, 244),
    "Na": ("Sodium", 11, 22.989),
    "Yb": ("Ytterbium", 70, 173.054),
    "Uus": ("Ununseptium", 117, 294),
    "Os": ("Osmium", 76, 190.23),
    "Rf": ("Rutherfordium", 104, 267),
    "P": ("Phosphorous", 15, 30.973),
    "B": ("Boron", 5, 10.81),
    "K": ("Potassium", 19, 39.0983),
    "In": ("Indium", 49, 114.818),
    "Pb": ("Lead", 82, 207.2),
    "Re": ("Rhenium", 75, 186.207),
    "Hs": ("Hassium", 108, 270),
    "Sg": ("Seaborgium", 106, 271),
    "Ti": ("Titanium", 22, 47.867),
    "Cr": ("Chromium", 24, 51.9961),
    "Co": ("Cobalt", 27, 58.933),
    "Cf": ("Californium", 98, 251),
    "Tb": ("Terbium", 65, 158.92),
    "Fe": ("Iron", 26, 55.845),
    "Fr": ("Francium", 87, 223),
    "Pd": ("Palladium", 46, 106.42),
    "Cn": ("Copernicium", 112, 285),
    "Ca": ("Calcium", 20, 40.078),
    "Bi": ("Bismuth", 83, 208.98),
    "C": ("Carbon", 6, 12.011),
    "Po": ("Polonium", 84, 209),
    "La": ("Lanthanum", 57, 138.90),
    "Lr": ("Lawrencium", 103, 262),
    "Ga": ("Gallium", 31, 69.723),
    "Se": ("Selenium", 34, 78.971),
    "Ni": ("Nickel", 28, 58.6934),
    "Fm": ("Fermium", 100, 257),
    "Y": ("Ytrium", 39, 88.90584),
    "As": ("Arsenic", 33, 74.921),
    "Te": ("Tellurium", 52, 127.60),
    "Ir": ("Iridium", 77, 192.217),
    "Nd": ("Neodymium", 60, 144.242),
    "N": ("Nitrogen", 7, 14.007),
    "Nb": ("Niobium", 41, 92.90637),
    "Tl": ("Thallium", 81, 204.38),
    "Cm": ("Curium", 96, 247),
    "Lv": ("Livermorium", 116, 293),
    "Th": ("Thorium", 90, 232.0377),
    "No": ("Nobelium", 102, 259),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Es": ("Einsteinium", 99, 252),
    "Mn": ("Manganese", 25, 54.938),
    "Np": ("Neptunium", 93, 237),
    "Sc": ("Scandium", 21, 44.955),
    "Rn": ("Radon", 86, 222),
    "Pt": ("Platinum", 78, 195.084),
    "W": ("Tungsten", 74, 183.84),
    "Mt": ("Meitnerium", 109, 276),
    "Lu": ("Lutetium", 71, 174.9668),
    "Ne": ("Neon", 10, 20.1797),
    "Pr": ("Praseodymium", 59, 140.90),
    "Mo": ("Molybdenum", 42, 95.95),
    "Ge": ("Germanium", 32, 72.63),
    "Uno": ("Ununoctium", 118, 294),
    "Bk": ("Berkelium", 97, 247),
    "Ba": ("Barium", 56, 137.327),
    "Gd": ("Gadolinium", 64, 157.25),
    "Tc": ("Technetium", 43, 98),
    "Sn": ("Tin", 50, 118.710),
    "Kr": ("Krypton", 36, 83.798),
    "V": ("Vanadium", 23, 50.9415),
    "Mg": ("Magnesium", 12, 24.305)
}


def getName(element):
    return ELEMENT_DATA[element][0]


def getAtomicNumber(element):
    return ELEMENT_DATA[element][1]


def getMolarMass(element):
    return ELEMENT_DATA[element][2]
