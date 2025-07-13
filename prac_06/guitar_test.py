from prac_06.guitar import Guitar

if __name__ == '__main__':
    guitar_1 = Guitar("Gibson L-5 CES", 1924, 16000)
    guitar_2 = Guitar("Another Guitar", 2013, 67)

    #Test get_age()
    expected_age_1 = 101
    actual_age_1 = guitar_1.get_age()
    print(f"{guitar_1.name} get_age() - Expected {expected_age_1}. Got {actual_age_1}")

    expected_age_2 = 12
    actual_age_2 = guitar_2.get_age()
    print(f"{guitar_2.name} get_age() - Expected {expected_age_2}. Got {actual_age_2}")

    #Test is_vintage()
    expected_vintage_1 = True
    actual_vintage_1 = guitar_1.is_vintage()
    print(f"{guitar_1.name} is_vintage() - Expected {expected_vintage_1}. Got {actual_vintage_1}")

    expected_vintage_2 = False
    actual_vintage_2 = guitar_2.is_vintage()
    print(f"{guitar_2.name} is_Vintage() - Expected {expected_vintage_2}. Got {actual_vintage_2}")