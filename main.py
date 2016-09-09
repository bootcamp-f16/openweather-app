from sys import argv, exit

from lib.app import App

def main():
    try:
        api_key = argv[1]
    except IndexError:
        print("Please pass in an API key for the Open Weather API.")
        exit(0)

    app = App(api_key)

    app.run()

if __name__ == '__main__':
    main()