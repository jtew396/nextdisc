import csv

disc_keys = {'NAME': ['SPEED', 'GLIDE', 'TURN', 'FADE']}
discs_owned = ['AVIAR', 'SHARK', 'LEOPARD', 'MAMBA', 'DESTROYER']
disc_data = {}
disc_diff_data = {}


def main():
    format_disc_data()
    for disc in disc_data:
        attribute_diffs = [50, 50]
        for i in [0,2]:
            if i == 0:
                min_diff = attribute_diffs[0]
            else:
                min_diff = attribute_diffs[1]
            for owned_disc in discs_owned:
                diff = abs((float(disc_data[owned_disc][i]) + float(disc_data[owned_disc][i + 1])) - (float(disc_data[disc][i]) + float(disc_data[disc][i + 1])))
                if diff < min_diff:
                    min_diff = diff
            if i == 0:
                attribute_diffs[0] = min_diff
            else:
                attribute_diffs[1] = min_diff
        disc_diff_data[disc] = attribute_diffs
    max_diff = 0
    second_diff = 0
    max_diff_discs = []
    second_diff_discs = []
    for disc in disc_diff_data:
        if sum(disc_diff_data[disc]) > max_diff:
            second_diff = max_diff
            second_diff_discs = max_diff_discs
            max_diff = sum(disc_diff_data[disc])
            max_diff_discs = []
            max_diff_discs.append(disc)
        elif sum(disc_diff_data[disc]) == max_diff:
            max_diff_discs.append(disc)
        elif sum(disc_diff_data[disc]) == second_diff:
            second_diff_discs.append(disc)
    print('Your next disc(s) is/are ' + str(max_diff_discs) + ' with a max difference of ' + str(max_diff) + ' points.')
    for disc in max_diff_discs:
        print(disc + ': ' + str(disc_data[disc]))
    print('The next most different disc(s) is/are ' + str(second_diff_discs) + ' with a max difference of ' + str(second_diff) + ' points.')
    for disc in second_diff_discs:
        print(disc + ': ' + str(disc_data[disc]))


def format_disc_data():
    with open('rawdiscdata.csv') as csvfile:
        datareader = csv.reader(csvfile, delimiter='\t')
        for row in datareader:
            disc_data[row[0]] = row[1:5]


if __name__ == "__main__":
    main()


'''
So we need to take the 5 discs that I have
(Aviar, Shark, Leopard, Mamba, and Destroyer)
then find the disc that is most different.
Take the abs value of the min difference for each characteristic.
Find the disc with the highest cumulative difference.
'''
