from collections import defaultdict

# Assuming each area now includes 'Rows' and 'indexLabel' for demonstration
areas = [
    {
        "Reversed":True,
        "id":  "01",
        "title": "Orange Top Left",
        "Rows": [[301, 304], [301, 304], [301, 305]],
        "indexLabel": ["A", "B", "C"],
        "name": "Orange",
        "disabledSeats": [
            { "row": 0, "col": 0 },
            { "row": 1, "col": 0 },
            { "row": 0, "col": 1 },
            { "row": 0, "col": 2 },
            { "row": 0, "col": 3 },
            { "row": 0, "col": 4 },
          ],
    },
    {

        "Reversed":True,
        "id":  "02",
        "title": "Orange Top Left Center",
        "Rows": [[101, 106], [101, 106], [101, 107], [101, 107]],
        "indexLabel": ["A", "B", "C", "D"],
        "name": "Orange",
        "disabledSeats": [
            { "row": 0, "col": 0 },
            { "row": 1, "col": 0 },
          ],
    },
    {
        "Reversed":False,
        "id":  "03",
        "title": "Orange Top Center",
        "Rows": [[1, 10], [1, 11], [1, 11], [1, 12]],
        "indexLabel": ["A", "B", "C", "D"],
        "name": "Orange",
        "disabledSeats": [
            { "row": 0, "col": 10 },
            { "row": 0, "col": 11 },
            { "row": 1, "col": 11 },
            { "row": 2, "col": 11 },
          ],
    },
    {
        "Reversed":False,
        "id":  "04",
        "title": "Orange Top Right Center",
        "Rows": [[201, 206], [201, 206], [201, 107], [201, 207]],
        "indexLabel": ["A", "B", "C", "D"],
        "name": "Orange",
        "disabledSeats": [
            { "row": 0, "col": 6 },
            { "row": 1, "col": 6 },
          ],
    },
    {
        "Reversed":False,
        "id":  "05",
        "title": "Orange Top Right",
        "Rows": [[401, 404], [401, 405], [401, 405]],
        "indexLabel": ["A", "B", "C"],
        "name": "Orange",
        "disabledSeats": [
            { "row": 0, "col": 4 },
            { "row": 1, "col": 4 },
            { "row": 0, "col": 1 },
            { "row": 0, "col": 2 },
            { "row": 0, "col": 3 },
            { "row": 0, "col": 0 },
          ],
    },
    {
        "Reversed":True,
        "id":  "06",
        "title": "Orange Center Left",
        "Rows": [
            [101, 108],
            [101, 108],
            [101, 109],
            [101, 110],
            [101, 110],
            [101, 111],
        ],
        "indexLabel": ["E", "F", "G", "H", "J", "K"],
        "name": "Orange",
        "disabledSeats": [
            { "row": 0, "col": 0 },
            { "row": 0, "col": 1 },
            { "row": 0, "col": 2 },
            { "row": 1, "col": 0 },
            { "row": 1, "col": 1 },
            { "row": 1, "col": 2 },
            { "row": 2, "col": 0 },
            { "row": 2, "col": 1 },
            { "row": 3, "col": 0 },
            { "row": 4, "col": 0 },
          ],
    },
    {
        "Reversed":False,
        "id":  "07",
        "title": "Orange Center Mid",
        "Rows": [[1, 12], [1, 12], [1, 12], [1, 13], [1, 13], [1, 13]],
        "indexLabel": ["E", "F", "G", "H", "J", "K"],
        "name": "Orange",
        "disabledSeats": [
            { "row": 0, "col": 12 },
            { "row": 1, "col": 12 },
            { "row": 2, "col": 12 },
          ],
    },
    {
        "Reversed":False,
        "id":  "08",
        "title": "Orange Center Right",
        "Rows": [
            [201, 208],
            [201, 208],
            [201, 209],
            [201, 210],
            [201, 210],
            [201, 211],
        ],
        "indexLabel": ["E", "F", "G", "H", "J", "K"],
        "name": "Orange",
        "disabledSeats": [
            { "row": 0, "col": 10 },
            { "row": 0, "col": 9 },
            { "row": 0, "col": 8 },
            { "row": 1, "col": 10 },
            { "row": 1, "col": 9 },
            { "row": 1, "col": 8 },
            { "row": 2, "col": 10 },
            { "row": 2, "col": 9 },
            { "row": 3, "col": 10 },
            { "row": 4, "col": 10 },
          ],
    },
    {
        "Reversed":True,
        "id":  "09",
        "title": "Green Top Left",
        "Rows": [
            [301, 306],
            [301, 306],
            [301, 307],
            [301, 307],
            [301, 308],
            [301, 308],
            [301, 308],
            [301, 308],
        ],
        "indexLabel": ["E", "F", "G", "H", "J", "K", "L", "M"],
        "name": "Green",
        "disabledSeats": [
            { "row": 0, "col": 0 },
            { "row": 0, "col": 1 },
            { "row": 1, "col": 0 },
            { "row": 1, "col": 1 },
            { "row": 2, "col": 0 },
            { "row": 3, "col": 0 },
          ],
    },
    {
        "Reversed":True,
        "id":  "10",
        "title": "Green Top Center left",
        "Rows": [[101, 111], [101, 111], [101, 112], [101, 112], [101, 112]],
        "indexLabel": ["L", "M", "N", "O", "P"],
        "name": "Green",
        "disabledSeats": [
            { "row": 0, "col": 0 },
            { "row": 1, "col": 0 },
          ],
    },
    {
        "Reversed":False,
        "id":  "11",
        "title": "Green Top Center Mid",
        "Rows": [[1, 13], [1, 13], [1, 13], [1, 13], [1, 13]],
        "indexLabel": ["L", "M", "N", "O", "P"],
        "name": "Green",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "12",
        "title": "Green Top Center Right",
        "Rows": [[201, 211], [201, 211], [201, 212], [201, 212], [201, 212]],
        "indexLabel": ["L", "M", "N", "O", "P"],
        "name": "Green",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "13",
        "title": "Green Top Right",
        "Rows": [
            [401, 406],
            [401, 406],
            [401, 407],
            [401, 407],
            [401, 408],
            [401, 408],
            [401, 408],
            [401, 408],
        ],
        "indexLabel": ["E", "F", "G", "H", "J", "K", "L", "M"],
        "name": "Green",
        "disabledSeats": [
            { "row": 0, "col": 7 },
            { "row": 0, "col": 6 },
            { "row": 1, "col": 7 },
            { "row": 1, "col": 6 },
            { "row": 2, "col": 7 },
            { "row": 3, "col": 7 },
          ],
    },
    {
        "Reversed":True,
        "id":  "14",
        "title": "Green Bottom Center Left",
        "Rows": [
            [101, 112],
            [101, 112],
            [101, 112],
            [101, 112],
            [101, 112],
            [101, 112],
        ],
        "indexLabel": ["Q", "R", "S", "T", "U", "V"],
        "name": "Green",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "15",
        "title": "Green Bottom Center",
        "Rows": [[1, 13], [1, 13], [1, 13]],
        "indexLabel": ["Q", "R", "S"],
        "name": "Green",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "16",
        "title": "Green Bottom Special",
        "Rows": [[1, 4], [1, 4], [1, 4]],
        "indexLabel": ["T", "U", "V"],
        "name": "Green",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "17",
        "title": "Purple Right",
        "Rows": [
            [401, 408],
            [401, 409],
            [401, 410],
            [401, 410],
            [401, 411],
            [401, 411],
            [401, 411],
            [401, 411],
            [401, 411],
        ],
        "indexLabel": ["N", "O", "P", "Q", "R", "S", "T", "U", "V"],
        "name": "Purple",
        "disabledSeats": [
            { "row": 0, "col": 10 },
            { "row": 0, "col": 9 },
            { "row": 0, "col": 8 },
            { "row": 1, "col": 10 },
            { "row": 1, "col": 9 },
            { "row": 2, "col": 10 },
            { "row": 3, "col": 10 },
          ],
    },
    {
        "Reversed":True,
        "id":  "18",
        "title": "Purple Left",
        "Rows": [
            [301, 308],
            [301, 309],
            [301, 310],
            [301, 310],
            [301, 311],
            [301, 311],
            [301, 311],
            [301, 311],
            [301, 311],
        ],
        "indexLabel": ["N", "O", "P", "Q", "R", "S", "T", "U", "V"],
        "name": "Purple",
        "disabledSeats": [
            { "row": 0, "col": 0 },
            { "row": 0, "col": 1 },
            { "row": 0, "col": 2 },
            { "row": 1, "col": 0 },
            { "row": 1, "col": 1 },
            { "row": 2, "col": 0 },
            { "row": 3, "col": 0 },
          ],
    },
    {
        "Reversed":False,
        "id":  "19",
        "title": "Green Bottom Right",
        "Rows": [
            [201, 212],
            [201, 212],
            [201, 212],
            [201, 212],
            [201, 212],
            [201, 212],
        ],
        "indexLabel": ["Q", "R", "S", "T", "U", "V"],
        "name": "Green",        
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "20",
        "title": "Yellow Bottom Left",
        "Rows": [[301, 311], [301, 311], [301, 311], [301, 311]],
        "indexLabel": ["W", "X", "Y", "Z"],
        "name": "Yellow",
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "21",
        "title": "Pink Top Left",
        "Rows": [[101, 112], [101, 112], [101, 112], [101, 112]],
        "indexLabel": ["W", "X", "Y", "Z"],
        "name": "Pink",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "22",
        "title": "Pink Top Center",
        "Rows": [[1, 13], [1, 13], [1, 13], [1, 13]],
        "indexLabel": ["W", "X", "Y", "Z"],
        "name": "Pink",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "23",
        "title": "Pink Top Right",
        "Rows": [[201, 212], [201, 212], [201, 212], [201, 212]],
        "indexLabel": ["W", "X", "Y", "Z"],
        "name": "Pink",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "24",
        "title": "Yellow Top Right",
        "Rows": [[401, 411], [401, 411], [401, 411], [401, 411]],
        "indexLabel": ["W", "X", "Y", "Z"],
        "name": "Yellow",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "25",
        "title": "Yellow Bottom Right",
        "Rows": [
            [401, 411],
            [401, 411],
            [401, 411],
            [401, 411],
            [401, 411],
            [401, 411],
            [401, 409],
            [401, 408],
        ],
        "indexLabel": ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH"],
        "name": "Yellow",
        "disabledSeats": [
            { "row": 6, "col": 10 },
            { "row": 6, "col": 9 },
            { "row": 7, "col": 10 },
            { "row": 7, "col": 9 },
            { "row": 7, "col": 8 },
          ],
    },
    {
        "Reversed":False,
        "id":  "26",
        "title": "Pink Bottom Right",
        "Rows": [
            [201, 212],
            [201, 212],
            [201, 212],
            [201, 212],
            [201, 212],
        ],
        "indexLabel": ["AA", "BB", "CC", "DD", "EE"],
        "name": "Pink",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "27",
        "title": "Pink Down Center",
        "Rows": [[1, 13], [1, 13], [1, 13], [1, 13], [1, 13]],
        "indexLabel": ["AA", "BB", "CC", "DD", "EE"],
        "name": "Pink",
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "28",
        "title": "Pink Bottom Left",
        "Rows": [
            [101, 112],
            [101, 112],
            [101, 112],
            [101, 112],
            [101, 112],
        ],
        "indexLabel": ["AA", "BB", "CC", "DD", "EE"],
        "name": "Pink",
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "29",
        "title": "Yellow Bottom Left",
        "Rows": [
            [301, 311],
            [301, 311],
            [301, 311],
            [301, 411],
            [301, 311],
            [301, 311],
            [301, 309],
            [301, 308],
        ],
        "indexLabel": ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH"],
        "name": "Yellow",
        "disabledSeats": [
            { "row": 6, "col": 0 },
            { "row": 6, "col": 1 },
            { "row": 7, "col": 0 },
            { "row": 7, "col": 1 },
            { "row": 7, "col": 2 },
          ],
    },
    {
        "Reversed":True,
        "id":  "30",
        "title": "Yellow Bottom Center Left",
        "Rows": [[101, 112], [101, 112], [101, 112]],
        "indexLabel": ["FF", "GG", "HH"],
        "name": "Yellow",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "31",
        "title": "Yellow Bottom Center Mid",
        "Rows": [[1, 13], [1, 13], [1, 13]],
        "indexLabel": ["FF", "GG", "HH"],
        "name": "Yellow",
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "32",
        "title": "Yellow Bottom Center Right",
        "Rows": [[201, 212], [201, 212], [201, 212]],
        "indexLabel": ["FF", "GG", "HH"],
        "name": "Yellow",
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "33",
        "title": "Loge Section 5",
        "name": "Yellow",
        "Rows": [[501, 507], [501, 507], [501, 507]],
        "indexLabel": ["A", "B", "C"],
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "34",
        "title": "Loge Section 3",
        "name": "Yellow",
        "Rows": [[301, 311], [301, 311], [301, 311]],
        "indexLabel": ["A", "B", "C"],
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "35",
        "title": "Loge Section 1",
        "name": "Yellow",
        "Rows": [[101, 111], [101, 111], [101, 111]],
        "indexLabel": ["A", "B", "C"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "36",
        "title": "Loge Section 2",
        "name": "Yellow",
        "Rows": [[201, 211], [201, 211], [201, 211]],
        "indexLabel": ["A", "B", "C"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "37",
        "title": "Loge Section 4",
        "name": "Yellow",
        "Rows": [[401, 411], [401, 411], [401, 411]],
        "indexLabel": ["A", "B", "C"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "38",
        "title": "Loge Section 6",
        "name": "Yellow",
        "Rows": [[601, 607], [601, 607], [601, 607]],
        "indexLabel": ["A", "B", "C"],
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "39",
        "title": "Loge Yellow Center Left",
        "name": "Yellow",
        "Rows": [[101, 114], [101, 114], [101, 114], [101, 114]],
        "indexLabel": ["D", "E", "F", "G"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "40",
        "title": "Loge Yellow Center Mid",
        "name": "Yellow",
        "Rows": [[1, 15], [1, 15], [1, 15], [1, 15]],
        "indexLabel": ["D", "E", "F", "G"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "41",
        "title": "Loge Yellow Center Right",
        "name": "Yellow",
        "Rows": [[201, 214], [201, 214], [201, 214], [201, 214]],
        "indexLabel": ["D", "E", "F", "G"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "42",
        "title": "Loge Purple Top Right",
        "name": "Purple",
        "Rows": [[401, 406], [401, 406], [401, 406], [401, 407],[401, 407]],
        "indexLabel": ["D", "E", "F", "G", "H"],
        "disabledSeats": [
              { "row": 0, "col": 6 },
              { "row": 1, "col": 6 },
              { "row": 2, "col": 6 },
            ],
    },
    {
        "Reversed":True,
        "id":  "43",
        "title": "Loge Purple Top Left",
        "name": "Purple",
        "Rows": [[301, 306], [301, 306], [301, 306], [301, 307],[301, 307]],
        "indexLabel": ["D", "E", "F", "G", "H"],
        "disabledSeats": [
              { "row": 0, "col": 0 },
              { "row": 1, "col": 0 },
              { "row": 2, "col": 0 },
            ],
    },
    {
        "Reversed":True,
        "id":  "44",
        "title": "Loge Purple Center Left",
        "name": "Purple",
        "Rows": [
            [101, 114],
            [101, 114],
            [101, 114],
            [101, 114],
            [101, 114],
            [101, 114],
            [101, 114],
            [101, 114],
            [101, 114],
        ],
        "indexLabel": ["H", "J", "K", "L", "M", "N", "O", "P", "Q"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "45",
        "title": "Loge Purple Center Mid",
        "name": "Purple",
        "Rows": [
            [1, 15],
            [1, 15],
            [1, 15],
            [1, 15],
            [1, 15],
            [1, 15],
            [1, 15],
            [1, 15],
            [1, 15],
        ],
        "indexLabel": ["H", "J", "K", "L", "M", "N", "O", "P", "Q"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "46",
        "title": "Loge Purple Center Right",
        "name": "Purple",
        "Rows": [
            [201, 214],
            [201, 214],
            [201, 214],
            [201, 214],
            [201, 214],
            [201, 214],
            [201, 214],
            [201, 214],
        ],
        "indexLabel": ["H", "J", "K", "L", "M", "N", "O", "P"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "47",
        "title": "Loge Gray Top Right",
        "name": "Gray",
        "Rows": [
            [401, 410],
            [401, 410],
            [401, 410],
            [401, 410],
            [401, 410],
            [401, 410],
            [401, 410],
        ],
        "indexLabel": ["K", "L", "M", "N", "O", "P", "Q"],
    },
    {
        "Reversed":True,
        "id":  "48",
        "title": "Loge Gray Top Left",
        "name": "Gray",
        "Rows": [
            [301, 310],
            [301, 310],
            [301, 310],
            [301, 310],
            [301, 310],
            [301, 310],
            [301, 310],
        ],
        "indexLabel": ["K", "L", "M", "N", "O", "P", "Q"],
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "49",
        "title": "Loge Gray Bottom Left",
        "name": "Gray",
        "Rows": [[301, 311], [301, 311], [301, 311]],
        "indexLabel": ["R", "S", "T"],
        "disabledSeats": [],
    },
    {
        "Reversed":True,
        "id":  "50",
        "title": "Loge Gray Bottom Center Left",
        "name": "Gray",
        "Rows": [[101, 114], [101, 114], [101, 114]],
        "indexLabel": ["R", "S", "T"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "51",
        "title": "Loge Gray Bottom Center Right",
        "name": "Gray",
        "Rows": [[206, 214], [206, 214], [206, 214], [206, 214]],
        "indexLabel": ["Q", "R", "S", "T"],
        "disabledSeats": [],
    },
    {
        "Reversed":False,
        "id":  "52",
        "title": "Loge Gray Bottom Right",
        "name": "Gray",
        "Rows": [[401, 411], [401, 411], [401, 415]],
        "indexLabel": ["R", "S", "T"],
        "disabledSeats": [
              { "row": 0, "col": 14 },
              { "row": 0, "col": 13 },
              { "row": 0, "col": 12 },
              { "row": 0, "col": 11 },
              { "row": 1, "col": 14 },
              { "row": 1, "col": 13 },
              { "row": 1, "col": 12 },
              { "row": 1, "col": 11 },
            ],
    },
]

# Prices and fees for each color - assuming these are given
prices_and_fees = {
    "Orange": {"price": "159.0", "fees": "28.42"},
    "Yellow": {"price": "99.0", "fees": "18.87"},
    "Green": {"price": "139.0", "fees": "25.24"},
    "Pink": {"price": "119.0", "fees": "22.05"},
    "Purple": {"price": "79.0", "fees": "15.69"},
    "Gray": {"price": "59.0", "fees": "12.50"},
}

# Modified grouping of areas by the 'name' attribute to include all area details
grouped_areas = defaultdict(list)
for area in areas:
    grouped_areas[area["name"]].append(area)  # Include entire area object


def is_seat_disabled(row, col, disabled_seats):
    """Check if a seat is disabled."""
    return any(seat for seat in disabled_seats if seat["row"] == row and seat["col"] == col)

def generate_seat_data(rows, indexLabel, disabled_seats, is_reversed=False):
    seat_data = []
    for row_idx, (row_range, label) in enumerate(zip(rows, indexLabel)):
        if is_reversed:
            columns = range(row_range[1], row_range[0] - 1, -1)
        else:
            columns = range(row_range[0], row_range[1] + 1)

        col_idx_adjusted = 0  # Initialize adjusted column index for subZoneTag
        for col_idx, seat_number in enumerate(columns):
            if not is_seat_disabled(row_idx, seat_number % 100, disabled_seats):
                seat_name = f"{label}{seat_number}"
                if is_reversed:
                    # For reversed, use the adjusted column index that increments correctly from the start
                    col_idx_adjusted += 1  # Increment adjusted column index for the next seat
                    sub_zone_tag = f"{row_idx},{col_idx_adjusted}"
                else:
                    sub_zone_tag = f"{row_idx},{col_idx}"
                seat_data.append({"name": seat_name, "subZoneTag": sub_zone_tag})

    return seat_data


def generate_gql_mutation_with_seats(grouped_areas, prices_and_fees):
    mutation = ["mutation CreateEvent {"]
    mutation.append("  createEvent(")
    mutation.append("    data: {")
    mutation.append('      description: "Soundtrack de la Naranja Mecanica en vivo.",')
    mutation.append('      name: "La Naranja Mecanica",')
    mutation.append("      eventZones: {")
    mutation.append("        create: [")

    for zone_name, areas in grouped_areas.items():
        mutation.append(
            f'          {{ name: "{zone_name}", fees: "{prices_and_fees[zone_name]["fees"]}", price: "{prices_and_fees[zone_name]["price"]}", eventZoneRows: {{ create: ['
        )
        for area in areas:
            seat_data = generate_seat_data(
                area["Rows"], area["indexLabel"], area.get("disabledSeats", []), area.get("Reversed", False))
            seats_str = ", ".join([f'{{ name: "{seat["name"]}", subZoneTag: "{seat["subZoneTag"]}" }}' for seat in seat_data])
            mutation.append(
                f'                {{ name: "{area["title"]}", eventSeats: {{ create: [{seats_str}] }} }},'
            )
        mutation.append("              ] } },")

    mutation.append("        ]")
    mutation.append("      }")
    mutation.append("    }")
    mutation.append("  ) {")
    mutation.append("    id")
    mutation.append("  }")
    mutation.append("}")

    return "\n".join(mutation)

# Generate the mutation string with variable prices, fees, dynamically generated seat names, and subZoneTags
corrected_mutation_str_with_subzone = generate_gql_mutation_with_seats(
    grouped_areas, prices_and_fees
)


# Generate the mutation string with variable prices, fees, and dynamically generated seat names
corrected_mutation_str = generate_gql_mutation_with_seats(
    grouped_areas, prices_and_fees
)

corrected_file_path = "corrected_gql_mutation.txt"
with open(corrected_file_path, "w") as file:
    file.write(corrected_mutation_str_with_subzone)

corrected_file_path
