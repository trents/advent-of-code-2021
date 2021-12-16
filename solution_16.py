''' Advent of Code 2021 Day 16 solution '''

def literal_processor(bstring):
    """ Returns two values: the value of the literal, and the remaining string """
    number_string = ""
    while True:
        number_string += bstring[1:5]
        sbit = bstring[0]
        bstring = bstring[5:]
        if sbit == "0":
            break
    return int(number_string,2), bstring
data = []

def packet_processor(bstring):
    """ General processor of packets """

    # set up initial variables
    packet_version = int(bstring[:3],2)
    packet_type = int(bstring[3:6],2)
    remainder = bstring[6:]
    data = []
    versions = 0
    result = 0

    if packet_type == 4: # handle a literal packet
        result, remainder = literal_processor(remainder)

    elif packet_type != 4:
        length_type = remainder[0]
        remainder = remainder[1:]
        sub_packets = []

        if length_type == "0": # next 15 bits represent total size of sub-packets
            sub_length = int(remainder[:15],2)
            remainder = remainder[15:]
            rem_length = len(remainder) - sub_length
            while len(remainder) > rem_length:
                sub, remainder = packet_processor(remainder)
                for pack in sub: sub_packets.append(pack)
        elif length_type == "1": # next 11 bits represent number of sub-packets
            sub_count = int(remainder[:11],2)
            remainder = remainder[11:]
            for _ in range(sub_count):
                sub, remainder = packet_processor(remainder)
                for pack in sub: sub_packets.append(pack)
        for x in sub_packets:
            versions += x[0]
        sub_results = []
        if packet_type == 0: # addition
            for x in sub_packets:
                result += x[2]
        elif packet_type == 1: # multiplication
            result = 1
            for x in sub_packets:
                result *= x[2]
        elif packet_type == 2: # minimum
            for x in sub_packets:
                sub_results += [x[2]]
            result = min(sub_results)
        elif packet_type == 3: # maximum
            for x in sub_packets:
                sub_results += [x[2]]
            result = max(sub_results)
        elif packet_type == 5: # greater than
            if sub_packets[0][2] > sub_packets[1][2]:
                result = 1
        elif packet_type == 6: # less than
            if sub_packets[0][2] < sub_packets[1][2]:
                result = 1
        elif packet_type == 7: # equal to
            if sub_packets[0][2] == sub_packets[1][2]:
                result = 1

    data.append((packet_version + versions, packet_type, result))    
    return data, remainder

def main():
    """ driver for solution to puzzle """
    with open('16.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]
    bstring = ""

    # I spent WAAAAAAY too long figuring this out
    # problem is that bin eats leading 0s, which screws up everything

    for char in lines[0]:
        x = bin(int(char,16))
        bstring += '0'*(6-len(x)) + str(x)[2:]

    counts, remainder = packet_processor(bstring)

    print("16a -> ",counts[-1][0])

    print("16b -> ",counts[-1][2])

if __name__ == "__main__":
    main()
