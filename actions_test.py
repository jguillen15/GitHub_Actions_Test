import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('number')
    args_dict = vars(parser.parse_args())
    number_retrieved = int(args_dict['number'])

    if number_retrieved > 10:
        print("Oops!")
        exit()
        #print("This should not be printed")
    else:
        print("All good :)")

if __name__ == '__main__':
    main()