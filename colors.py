import random


COLORS = {
    'blueviolet': "8A2BE2",
    'brown': "A52A2A",
    'cadetblue': "5F9EA0",
    'chocolate': "D2691E",
    'coral': "FF7F50",
    'cornflowerblue': "6495ED",
    'crimson': "DC143C",
    'darkblue': "00008B",
    'darkcyan': "008B8B",
    'darkgoldenrod': "B8860B",
    'darkgreen': "006400",
    'darkmagenta': "8B008B",
    'darkolivegreen': "556B2F",
    'darkorange': "FF8C00",
    'darkorchid': "9932CC",
    'darksalmon': "E9967A",
    'darkslateblue': "483D8B",
    'darkslategrey': "2F4F4F",
    'darkviolet': "9400D3",
    'deeppink': "FF1493",
    'deepskyblue': "00BFFF",
    'dimgray': "696969",
    'dodgerblue': "1E90FF",
    'firebrick': "B22222",
    'forestgreen': "228B22",
    'fuchsia': "FF00FF",
    'goldenrod': "DAA520",
    'gray': "808080",
    'green': "008000",
    'indianred': "CD5C5C",
    'indigo': "4B0082",
    'lightcoral': "F08080",
    'lightseagreen': "20B2AA",
    'limegreen': "32CD32",
    'maroon': "800000",
    'mediumblue': "0000CD",
    'mediumorchid': "BA55D3",
    'mediumpurple': "9370D8",
    'mediumseagreen': "3CB371",
    'mediumslateblue': "7B68EE",
    'mediumvioletred': "C71585",
    'midnightblue': "191970",
    'navy': "000080",
    'olivedrab': "6B8E23",
    'orange': "FFA500",
    'orangered': "FF4500",
    'orchid': "DA70D6",
    'peru': "CD853F",
    'purple': "800080",
    'rebeccapurple': "663399",
    'red': "FF0000",
    'royalblue': "4169E1",
    'salmon': "FA8072",
    'sandybrown': "F4A460",
    'seagreen': "2E8B57",
    'sienna': "A0522D",
    'slateblue': "6A5ACD",
    'slategrey': "708090",
    'steelblue': "4682B4",
    'teal': "008080",
    'violet': "EE82EE",
    'yellowgreen': "9ACD32"
}

NEW_COLORS = [
    # original, darker, lighter
    ('#2E4372', '#1E3360', '#405583'),
    ('#0135D1', '#01289E', '#0C48FA'),
    ('#0165CD', '#014B99', '#087FFA'),
    ('#00A296', '#007E75', '#18B4A9'),
    ('#ED1100', '#BF0E00', '#FF1300'),
    ('#BA1E2A', '#9B0D17', '#D43D48'),
    ('#CF003B', '#A90030', '#E6225A'),
    ('#650A1E', '#4D0313', '#831A30'),
    ('#6D6D0B', '#545403', '#8D8D1C'),
    ('#47650A', '#354E03', '#60841A'),
    ('#235D0A', '#174802', '#357918'),
    ('#166841', '#09512E', '#237B51'),
    ('#28A514', '#1E8E0D', '#38BC24'),
    ('#C75118', '#AC420F', '#E3672B'),
    ('#E26400', '#C35600', '#FF7100'),
    ('#D09B00', '#B58600', '#F4B600'),
    ('#EC9300', '#C87D00', '#FFA612'),
    ('#4A0DA0', '#3F0B88', '#5B1CB4'),
    ('#75069C', '#630584', '#8713B0'),
    ('#A6008C', '#8D0077', '#BA0D9F'),
    ('#7E3EA9', '#702F9D', '#9051BA'),
    ('#CC58A1', '#BC4490', '#D96EB2'),
    ('#E19851', '#CC833C', '#F8B16B'),
    ('#762323', '#5F1616', '#8C3333'),
    ('#7B3302', '#5D2600', '#96460F'),
    ('#401746', '#330F38', '#4D2153'),
    ('#343841', '#22252B', '#424753'),
    ('#A63E4E', '#8E2D3D', '#C25365'),
    ('#B06441', '#965030', '#CE7D58'),
    ('#B08741', '#967130', '#CEA258')
]


def get_colors(number):
    return random.sample(COLORS, number)


def randomize_colors():
    random.shuffle(NEW_COLORS)
    return NEW_COLORS
